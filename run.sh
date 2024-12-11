#!/bin/bash

action=$1  # Acción principal (-e, -c)
env=$2     # Entorno (dev, prod)
SERVICE_NAME="mini-retro-cam"  # Nombre del servicio definido en docker-compose.yml

trap "exit_apps" 2

function exit_apps () {
  echo -e "\nCERRANDO APLICACIÓN...\n"
  docker compose stop -t 1
  exit 0
}

function is_container_existing () {
  # Verifica si el contenedor ya existe
  docker ps -a --filter "name=${SERVICE_NAME}" --format "{{.Names}}" | grep -q "${SERVICE_NAME}"
}

if [ ! -z $action ]; then

  # "-e" para ejecutar en diferentes entornos
  if [ $action = -e ]; then
    if [[ $env == "dev" ]]; then
      echo -e "\nEJECUTANDO EN MODO DESARROLLO...\n"
      if is_container_existing; then
        docker compose -f docker-compose.yml up
      else
        docker compose -f docker-compose.yml up --build
      fi
    elif [[ $env == "prod" ]]; then
      echo -e "\nEJECUTANDO EN MODO PRODUCCIÓN...\n"
      if is_container_existing; then
        docker compose -f docker-compose-prod.yml up
      else
        docker compose -f docker-compose-prod.yml up --build
      fi
    else
      echo "Por favor, especifica el entorno (dev o prod)."
    fi

  else
    echo "Acción no válida. Usa -e para ejecutar o -c para compilar."
  fi

else
  echo "Debes proporcionar una acción (-e para ejecutar, -c para compilar)."
fi
