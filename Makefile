#!/usr/bin/env make

APPID=your-app-id-here

run:
	gcloud preview app run go-frontend py-backend

deploy:
	gcloud preview app deploy --project=$(APPID) go-frontend py-backend
