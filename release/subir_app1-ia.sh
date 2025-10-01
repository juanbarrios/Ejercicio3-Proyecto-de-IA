#!/bin/bash

AMBIENTE="ejercicio3"
APP="app1-ia"
PORT=7002

RUTA_APP="$HOME/ejercicio3/$APP"
RUTA_SERVER="$HOME/ejercicio3/apache-$APP"
RUTA_LOGS="$HOME/ejercicio3/logs"

source "$HOME/miniforge3/bin/activate" "$AMBIENTE" && \
cd "$RUTA_APP" && \
mkdir -p "$RUTA_LOGS" && \
mod_wsgi-express start-server application.wsgi --port $PORT \
      --server-root "$RUTA_SERVER" \
      --access-log --log-to-terminal \
       2>&1 | /usr/bin/cronolog "$RUTA_LOGS/$APP.%Y-%m-%d.log"
