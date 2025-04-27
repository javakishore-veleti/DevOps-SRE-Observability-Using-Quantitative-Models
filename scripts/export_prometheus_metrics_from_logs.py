#!/usr/bin/env python3

"""
Export Prometheus metrics by parsing HTTP Access Logs or Application Logs.

This script reads logs, extracts important observability fields (like response time and status code),
and exposes them on a /metrics endpoint that Prometheus can scrape.

Usage:
    python export_prometheus_metrics_from_logs.py --logfile /path/to/access.log

Author: javakishore-veleti (DevOps-SRE-Observability-Using-Quantitative-Models Project)
License: MIT
"""

import time
import argparse
from prometheus_client import start_http_server, Gauge, Counter

import re

# Define Prometheus Metrics
http_response_time_gauge = Gauge('exported_http_response_time_seconds', 'HTTP Response Time extracted from logs', ['method', 'endpoint'])
http_status_counter = Counter('exported_http_status_total', 'HTTP Status codes extracted from logs', ['status_code'])

# Example Log Line Pattern
log_pattern = re.compile(
    r'(?P<method>GET|POST|PUT|DELETE)\s(?P<uri>/\S*)\s.*\s(?P<status>\d{3})\s(?P<response_time>\d+\.\d+)'  # Simplified pattern
)

def parse_log_line(line):
    """Parse a log line and extract method, endpoint, status, and response time."""
    match = log_pattern.search(line)
    if match:
        method = match.group('method')
        uri = match.group('uri')
        status = match.group('status')
        response_time = float(match.group('response_time'))
        return method, uri, status, response_time
    return None

def tail_log_and_export(logfile_path):
    """Tail the log file and export parsed metrics."""
    with open(logfile_path, 'r') as f:
        f.seek(0, 2)  # Go to end of file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue

            parsed = parse_log_line(line)
            if parsed:
                method, uri, status, response_time = parsed

                # Update Prometheus metrics
                http_response_time_gauge.labels(method=method, endpoint=uri).set(response_time)
                http_status_counter.labels(status_code=status).inc()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Prometheus metrics from HTTP access logs.")
    parser.add_argument('--logfile', required=True, help='Path to the HTTP access log file')
    parser.add_argument('--port', type=int, default=9105, help='Port to expose metrics on (default: 9105)')

    args = parser.parse_args()

    # Start Prometheus HTTP server
    start_http_server(args.port)
    print(f"Started Prometheus metrics exporter on port {args.port}... Parsing log file: {args.logfile}")

    # Start parsing and exporting
    tail_log_and_export(args.logfile)
