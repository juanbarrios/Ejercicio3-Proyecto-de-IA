#!/bin/bash
ACCION="$1"

if [[ "$ACCION" != "web" && "$ACCION" != "servicios" ]]; then
        echo "Error: Accion desconocida $ACCION"
        echo "Acciones validas: web servicios"
        exit 1
fi

function runTest() {
        echo "[`date "+%F %T"`]\$ $@"
        "$@"
        if [[ $? -ne 0 ]]; then
                echo "** ERROR IN $@"
                exit 1
        fi
}

cd `dirname "$0"`
BASE_DIR=`pwd`

if [[ "$ACCION" == "web" ]]; then
    APPS_DESTINATION="$HOME/ejercicio3"
    runTest mkdir -p "$APPS_DESTINATION"
    for app in app1-front app1-ia app2-front app2-ia
    do
        echo "instalando $app en $APPS_DESTINATION ..."
        if [[ -f "$APPS_DESTINATION/bajar_$app.sh" ]]; then
            runTest bash "$APPS_DESTINATION/bajar_$app.sh"
        fi
        runTest cp -r "../$app/" "$APPS_DESTINATION/"
        runTest cp "subir_$app.sh" "bajar_$app.sh" "$APPS_DESTINATION"
        runTest chmod +x "$APPS_DESTINATION/subir_$app.sh" "$APPS_DESTINATION/bajar_$app.sh"
        runTest bash "$APPS_DESTINATION/subir_$app.sh"
    done
    echo "ok $ACCION"
elif [[ "$ACCION" == "servicios" ]]; then
    SERVICES_DIR="$HOME/.config/systemd/user/"
    runTest mkdir -p "$SERVICES_DIR"
    runTest cp server_app1-front.service server_app1-ia.service server_app2-front.service server_app2-ia.service "$SERVICES_DIR"
    runTest systemctl --user daemon-reload
    runTest systemctl --user enable server_app1-front
    runTest systemctl --user enable server_app1-ia
    runTest systemctl --user enable server_app2-front
    runTest systemctl --user enable server_app2-ia
    runTest loginctl enable-linger
    echo "ok $ACCION"
fi
