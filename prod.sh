#!/bin/bash
FLASK_PRODUCTION=true
WORKDIR="/srv/natixone_api"
cd $WORKDIR
source ./venv/bin/activate
gunicorn --workers=2 --bind 0.0.0.0:5000 app:app