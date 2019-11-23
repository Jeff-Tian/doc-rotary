#!/usr/bin/env bash

heroku container:push web -a doc-rotary
heroku container:release web -a doc-rotary
heroku open -a doc-rotary
