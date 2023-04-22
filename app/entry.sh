#!/bin/sh

cd /app
/usr/bin/env uvicorn --host 0.0.0.0 --port 8080 --workers 2 backend:app