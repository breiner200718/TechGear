#!/bin/bash

pip install -r requirements.txt

cd techgear_web

python manage.py collectstatic --noinput