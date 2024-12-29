#!/bin/bash
FLASK_PRODUCTION=true
WORKDIR="/srv/natixone_api"
cd $WORKDIR
source $WORKDIR/venv/bin/activate
$WORKDIR/venv/bin/gunicorn -w 2 --bind 0.0.0.0:5000 app:app