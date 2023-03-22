from fastapi import FastAPI, Header, Request
from fastapi.responses import JSONResponse

from .config import config
from .models import PingBody, PackageBody
from .utils import validate_signature

app = FastAPI()


@app.post("/")
async def hello_world(
    body: PingBody | PackageBody,
    request: Request,
    x_github_event: str = Header(),
):
    if not await validate_signature(request):
        return JSONResponse(content={"message": "Invalid signature"}, status_code=401)

    if x_github_event == "package":
        assert type(body) == PackageBody, "Invalid body for event"
        package_body: PackageBody = body  # type: ignore

        if (
            package_body.package.package_version
            and package_body.package.package_version.container_metadata
            and package_body.package.package_version.container_metadata.tag.name
            == "latest"
        ):
            # TODO: actually run command
            return config.command
            # return check_output(config.command)
        else:
            return "Nothing to do for this version"
    return "Nothing to do"
