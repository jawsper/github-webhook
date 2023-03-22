# github-webhook

A small FastAPI app that can accept Github webhooks

Currently only types implemented:
* ping (partially)
* package

The app will execute a script (from env `COMMAND`) whenever a package is released that matches env `MATCH_TAG` (default "latest").

The Github secret can be passed with env var `GITHUB_SECRET`.

## Running
You can run it with `python -m webhook` or `uvicorn webhook:app`
