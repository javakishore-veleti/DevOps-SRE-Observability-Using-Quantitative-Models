# Microservices Sample Application Logs for Observability Modeling

This folder provides **sample logs** and **instructions** to simulate real-world microservices observability environments.

The logs can be used to demonstrate how to extract metrics, build dashboards, and create alerts based on **Linear**, **Power**, **Exponential**, and **Logarithmic** growth models.

---

## Files

| File | Purpose |
|:-----|:--------|
| `sample-access-logs.log` | Simulated HTTP server access logs (GET/POST requests, response times, status codes). |
| `sample-application-logs.log` | Simulated Java SLF4J application logs (INFO, WARN, ERROR levels, exceptions). |
| `instructions-to-use-logs.md` | Step-by-step guide on how to extract metrics from logs, create dashboards, and build alert rules using the provided samples. |

---

## Usage Instructions

1. Follow the steps in `instructions-to-use-logs.md` to:
   - Parse the sample logs.
   - Export metrics for Prometheus scraping.
   - Build visualizations in Grafana and Kibana.
   - Apply Prometheus alerting rules.

2. Metrics and modeling examples:
   - HTTP Response Time → Linear and Power modeling.
   - HTTP Status Code Errors → Exponential modeling.
   - Application Errors and Failures → Exponential and Power modeling.

3. Extend the logs as needed:
   - Add more success/failure scenarios.
   - Simulate high-traffic bursts or gradual load increases.

---

## Intended Audience

- DevOps Engineers
- Site Reliability Engineers (SREs)
- Observability Architects
- Software Developers interested in production monitoring and reliability

---

## Notes

- These logs are **static examples** for educational and testing purposes.
- Actual production systems would generate continuous log streams.
- Log formats used here are simplified versions of common microservice logging and HTTP access standards.

---
