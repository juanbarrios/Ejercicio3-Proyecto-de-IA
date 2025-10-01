#!/bin/bash

AMBIENTE="ejercicio3"
APP="app2-ia"
PORT=7012

RUTA_APP="$HOME/ejercicio3/$APP"
RUTA_SERVER="$HOME/ejercicio3/apache-$APP"
RUTA_LOGS="$HOME/ejercicio3/logs"

function runTest() {
        echo "[`date "+%F %T"`]\$ $@"
        "$@"
        if [[ $? -ne 0 ]]; then
                echo "** ERROR IN $@"
                exit 1
        fi
}

runTest source "$HOME/miniforge3/bin/activate" "$AMBIENTE"
runTest cd "$RUTA_APP"
runTest mkdir -p "$RUTA_LOGS"
runTest mod_wsgi-express start-server application.wsgi \
                         --port $PORT \
                         --server-root "$RUTA_SERVER" \
                         --access-log --log-to-terminal \
                          2>&1 | /usr/bin/cronolog "$RUTA_LOGS/$APP.%Y-%m-%d.log"
