# Tools Mapping Guide for Quantitative Modeling

This guide explains how different Observability tools — **Prometheus**, **Grafana**, and **Kibana** — support applying **Linear**, **Power**, **Exponential**, and **Logarithmic** modeling to real-world microservices monitoring.

Mapping the right tool capabilities to the right model helps design smarter dashboards, queries, and alerts.

---

## Tool vs Modeling Capabilities

| Modeling Type | Prometheus | Grafana | Kibana |
|:--------------|:-----------|:--------|:-------|
| **Linear** | `rate()`, `increase()` functions for steady trend detection. | Visualizations with threshold lines and trend projections. | Derivative and moving average aggregations to observe steady changes. |
| **Power** | Custom expressions using `rate()` and manual exponent math. | Math transformations (e.g., `metric^1.5`) in panels. | Scripted fields using `Math.pow()` in runtime fields or Lens formulas. |
| **Exponential** | `exp()` function on rates or error totals. | Exponential smoothing in moving average panels. | Exponential weighted moving averages (through Lens or custom aggregations). |
| **Logarithmic** | `log()` function on metric rates. | Logarithmic Y-axis scaling and log-based transformations. | Log-scale Y-axis, scripted log fields using `Math.log()`. |

---

## How Each Tool Helps

### Prometheus
- **Mathematical expressions** (`exp()`, `log()`, manual powers) allow transforming metric behavior directly at the query level.
- **Recording rules** let you store intermediate calculated trends for efficient alerting.

### Grafana
- **Flexible visualization**: apply math transformations, moving averages, threshold bands, and log-scaled visualizations easily.
- **Panel alerts**: detect trend shifts without needing complicated queries.

### Kibana
- **Powerful log analysis and field transformations**: create runtime fields to apply logarithmic, exponential, or power formulas on extracted fields.
- **Lens and TSVB (Time Series Visual Builder)** support trend exploration with smoothing and scaling options.

---

## Example Use Cases

| Scenario | Model | Tool and Method |
|:---------|:------|:----------------|
| Monitor CPU growth vs traffic | Linear | Prometheus `rate()` and Grafana threshold panel. |
| Detect application slowdown under load | Power | Grafana math transformation panel (`metric ^ 1.5`). |
| Alert on sudden error explosions | Exponential | Prometheus `exp(rate(error_total[5m]))` with alert rule. |
| Visualize optimization diminishing returns | Logarithmic | Kibana log-scale Lens dashboard showing latency gains flattening. |

---

## Best Practices

- **Start simple** (Linear monitoring) and only introduce more complex models (Power, Exponential) when system behavior demands it.
- **Tune transformations carefully**: wrong math can make healthy systems look unhealthy.
- **Always validate modeled metrics** against historical data before enabling alerts.
- **Document dashboards** so that team members understand why math transformations were applied.

---
