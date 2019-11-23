#!/usr/bin/env bash
cd webapp
pip3 install -r requirements.txt
cd ..
python3 webapp/app.py
