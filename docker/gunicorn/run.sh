#!/bin/bash

cd /www/tizen_rest_api/TizenRestApi/
source /www/tizen_rest_api/env_py38
pip install -r requirements.txt

gunicorn --workers 4 --bind 0.0.0.0:8000 TizenRestApi.wsgi:application --daemon --reload

while true; 
do 
    echo "still live"; 
    sleep 600; 
done
