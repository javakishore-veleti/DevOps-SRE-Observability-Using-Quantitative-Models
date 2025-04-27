
# Kibana Visualizations for DevOps and SRE Observability

This folder contains Kibana visualizations focused on analyzing HTTP error rates and HTTP latency trends. These visualizations help DevOps and SRE teams apply quantitative modeling principles to real-world microservices observability.

---

## Files

| File | Purpose |
|:-----|:--------|
| **error-rate-visualizations.ndjson** | Visualizes HTTP 4xx and 5xx error rates over time to detect early signs of service degradation or cascading failures. |
| **http-latency-visualizations.ndjson** | Visualizes HTTP response time trends, including average, p90, and p99 latencies to monitor slowdowns and ensure SLO compliance. |

---

## Visualizations Overview

### error-rate-visualizations.ndjson
- **HTTP Error Rate % Over Time** (Line chart)
- **5xx Server Errors Count** (Bar chart)
- **4xx vs 5xx Error Trends** (Stacked area chart)

### http-latency-visualizations.ndjson
- **Average HTTP Response Time** (Line chart)
- **P90 and P99 Latency Trends** (Area chart)
- **Latency Breakdown by HTTP Method** (Bar chart)

---

## Usage

1. Go to **Kibana → Stack Management → Saved Objects**.
2. Click **Import** and select the `.ndjson` files.
3. Open the imported visualizations under **Visualize Library**.
4. Add them to dashboards or use them directly for analysis.

> **Note:**  
> Make sure your index patterns match fields like `http.response.status_code`, `http.response_time`, and `@timestamp`.  
> (You may need to adjust field names depending on your log ingestion setup.)

---

## Objective

These visualizations are designed to:

- Detect **exponential growth in error rates** early.
- Track **linear and non-linear latency growth**.
- Support **SLO monitoring**, **anomaly detection**, and **early alerting** based on quantitative modeling insights.

---

