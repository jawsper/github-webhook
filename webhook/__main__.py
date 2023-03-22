import click
import uvicorn

from .app import app


@click.command()
@click.argument("host", default="localhost")
@click.option("--port", default=8080, type=int)
def main(host, port):
    """Start a HTTPServer which waits for requests."""
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
