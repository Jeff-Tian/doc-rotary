#!/usr/bin/env bash

heroku container:push web -a bitqbit
heroku container:release web -a bitqbit
heroku open -a bitqbit
