# appengine-multiple-runtimes-sample
Sample repository that show how to use Modules to run a Go frontend and a Python backend.

## Requirements

Install Google Cloud SDK and some components to work with App Engine:

	curl https://sdk.cloud.google.com/ | bash
	gcloud components update pkg-go pkg-python preview app

## Running and deploying

Just run the modules using the `gcloud` tool, or use the provided Makefile:

	make run

This starts the local development server for both modules.
Allows you to emulate the same shared state, like, they will use the same datastore.

	make deploy

Updates all modules to the production.
