# Instructions to Use Sample Logs for Observability Modeling

This document explains how to use the provided **sample access logs** and **application logs** to build Prometheus metrics, Grafana dashboards, and Kibana visualizations that apply Linear, Power, Exponential, and Logarithmic modeling techniques.

---

## 1. Files Provided

| File | Purpose |
|:-----|:--------|
| `sample-access-logs.log` | Simulates HTTP server access logs for microservices (status codes, response times, endpoints). |
| `sample-application-logs.log` | Simulates Java SLF4J application logs (INFO, WARN, ERROR logs, exceptions). |

---

## 2. Extracting Metrics from Logs

Use the provided script `scripts/export_prometheus_metrics_from_logs.py` to parse logs and expose Prometheus metrics.

### Example Metric Extractions:

| From | Metric | Modeling Type |
|:-----|:-------|:--------------|
| Access Logs | HTTP Response Time (`exported_http_response_time_seconds`) | Linear (normal latency), Power (slowdowns under load) |
| Access Logs | HTTP Status Codes (`exported_http_status_total`) | Exponential (error bursts), Linear (normal errors) |
| Application Logs | Error Counts (parsed from ERROR lines) | Exponential (failure cascades) |
| Application Logs | Log Level Volume (INFO/WARN/ERROR counts) | Power or Exponential (depending on growth patterns) |

---

## 3. Setting up Prometheus Scraping

After running the exporter script:

```bash
python scripts/export_prometheus_metrics_from_logs.py --logfile /path/to/sample-access-logs.log --port 9105
