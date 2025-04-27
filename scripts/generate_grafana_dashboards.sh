#!/bin/bash

# Script to import Grafana dashboards into a running Grafana server.
# 
# Author: javakishore-veleti (DevOps-SRE-Observability-Using-Quantitative-Models Project)
# License: MIT

GRAFANA_HOST="http://localhost:3000"
GRAFANA_API_KEY=""  # <-- Replace with your Grafana API Key or pass via --api-key argument
DASHBOARDS_DIR="./dashboards/grafana"

# Helper function
usage() {
  echo "Usage: $0 --api-key <GRAFANA_API_KEY>"
  exit 1
}

# Parse arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --api-key)
      GRAFANA_API_KEY="$2"
      shift
      shift
      ;;
    *)
      usage
      ;;
  esac
done

if [ -z "$GRAFANA_API_KEY" ]; then
  echo "Grafana API Key is required."
  usage
fi

# Import dashboards
for file in "$DASHBOARDS_DIR"/*.json; do
  echo "Importing dashboard: $file"

  curl -s -X POST "$GRAFANA_HOST/api/dashboards/db" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GRAFANA_API_KEY" \
    -d @"$file"

  if [ $? -eq 0 ]; then
    echo "Successfully imported $file"
  else
    echo "Failed to import $file"
  fi
done
