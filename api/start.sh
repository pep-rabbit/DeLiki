#!/bin/sh
set -e

echo "Starting user application..."
exec granian src.main:app \
    --host 0.0.0.0 \
    --port 8080 \
    --interface asgi
