import logging
import shlex
from subprocess import Popen, SubprocessError
from typing import Union

from fastapi import FastAPI, Header

from .config import config
from .middleware import ValidateSignatureMiddleware
from .models import PingBody, PackageBody

log = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(ValidateSignatureMiddleware)


@app.post("/")
async def hello_world(
    body: Union[PingBody, PackageBody],
    x_github_event: str = Header(),
):
    if x_github_event == "package":
        assert type(body) == PackageBody, "Invalid body for event"
        package_body: PackageBody = body  # type: ignore

        if (
            package_body.package.package_version
            and package_body.package.package_version.container_metadata
            and package_body.package.package_version.container_metadata.tag.name
            == config.match_tag
        ):
            try:
                process = Popen(shlex.split(config.command))
                return "Process started"
            except SubprocessError as e:
                log.exception("Error calling process")
                return "Failed to execute command"

        else:
            return "Nothing to do for this version"
    return "Nothing to do"
