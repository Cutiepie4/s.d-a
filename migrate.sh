#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

cd "$1"
python3 manage.py makemigrations
python3 manage.py migrate