#!/bin/sh

export $(grep -v '^#' .env | xargs)

python3 app.py
