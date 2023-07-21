from starlette.requests import Request
from starlette.exceptions import HTTPException
from starlette.types import ASGIApp, Receive, Scope, Send

from .utils import validate_signature


class ValidateSignatureMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        request = Request(scope)
        signature = request.headers.get("x-hub-signature-256")
        body: bytes = b""

        async def receive_wrapper():
            nonlocal body
            message = await receive()
            assert message["type"] == "http.request"
            body += message.get("body", b"")

            if not message.get("more_body", False):
                if not validate_signature(signature, body):
                    raise HTTPException(401, "Invalid signature")

            return message

        await self.app(scope, receive_wrapper, send)
