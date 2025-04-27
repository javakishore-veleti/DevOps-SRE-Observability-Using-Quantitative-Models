# Prometheus Alerting Rules for Observability Modeling

This folder contains Prometheus alerting rules designed to detect system behavior based on **Quantitative Modeling** techniques: Linear, Power, and Exponential growth patterns.

Each alert rule helps DevOps and SRE teams identify early warning signals before critical incidents occur.

---

## Available Alert Rules

| File | Purpose |
|:-----|:--------|
| **exponential_error_spike_alerts.yml** | Detects rapid exponential growth of 5xx server errors or application exceptions. Helps catch cascading failures early. |
| **linear_rule_alerts.yml** | Monitors steady, predictable growth in CPU usage, memory usage, and HTTP response latency. Ideal for capacity planning and early warnings. |
| **power_performance_bottleneck_rules.yml** | Detects performance degradation that grows faster than traffic (power model behavior). Useful for identifying early system bottlenecks under load. |

---

## How to Use

1. Copy the desired `.yml` files into your Prometheus server configuration directory.
2. Include them inside your `prometheus.yml` configuration under the `rule_files` section.
3. Ensure your Prometheus instance has access to the right metrics:
   - `http_requests_total`
   - `http_request_duration_seconds_sum`
   - `http_request_duration_seconds_count`
   - `process_cpu_seconds_total`
   - `node_memory_MemAvailable_bytes`, `node_memory_MemTotal_bytes`
4. Reload Prometheus or restart the service after updating rule files.

---

## Best Practices

- **Adjust thresholds** (`0.05`, `0.002`, etc.) according to your system’s normal behavior baselines.
- **Tune `for:` durations** (e.g., 2 minutes, 5 minutes) to balance between early detection and alert noise.
- **Route alerts** to proper notification channels (Slack, PagerDuty, OpsGenie) based on `severity` and `team` labels.
- **Combine with dashboards** in Grafana for richer visualization and context.

---
