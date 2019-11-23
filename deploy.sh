#!/usr/bin/env bash

heroku container:push web -a doc-rotarybit
heroku container:release web -a doc-rotarybit
heroku open -a doc-rotarybit
