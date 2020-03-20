#!/bin/sh

if ! [[ -d "./venv" ]]
then
    echo "virtual environment does not yet exist. creating..."
    python -m venv venv
fi

source venv/bin/activate

pip install -r requirements.txt