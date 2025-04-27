# DevOps and SRE Observability Using Quantitative Models

![Built with Prometheus](https://img.shields.io/badge/Built%20With-Prometheus-orange)
![Built with Grafana](https://img.shields.io/badge/Built%20With-Grafana-yellowgreen)
![Built with Kibana](https://img.shields.io/badge/Built%20With-Kibana-blue)
![Inspired by Coursera](https://img.shields.io/badge/Inspired%20By-Coursera-blueviolet)
![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen)

---

## Inspiration

This project is inspired by the Coursera course **"Fundamentals of Quantitative Modeling"**. During my learning journey, I was fascinated by how modeling techniques could extend beyond traditional domains like finance or data science, and be applied meaningfully to **Observability of Microservices** using tools like **Kibana**, **Grafana**, and **Prometheus**.

A huge thank you to the course instructors for providing a strong foundation in modeling principles!

---

## Assumptions

- You are already capturing **HTTP Access Logs** and **Application Logs** from your microservices built in **Java**, **.NET**, **Python**, **Node.js**, or **Scala**.

---

## Introduction to Modeling Types

| Model Type | Purpose | Why This Model Type |
|------------|---------|---------------------|
| **Linear** | Models steady, predictable changes (e.g., CPU usage growing proportionally to load). | Easy to spot steady growth, simple alerts and predictions. |
| **Power** | Models systems where behavior grows faster as input grows (e.g., response time degradation). | Useful for detecting performance bottlenecks as traffic increases. |
| **Exponential** | Models rapid growth patterns (e.g., cascading failures, sudden spikes). | Good for catching sudden spikes early before they cause outages. |
| **Logarithmic** | Models situations where early changes are big, but later changes slow down (e.g., system optimizations). | Helps visualize slowing improvements or gains clearly over time. |

### Visual Guide: Growth Shapes

![Visual Guide - Growth Shapes](./visual-guide-growth-shapes.png)

---

## Introduction to Observability Tools

| Tool            | Purpose |
|-----------------|---------|
| **Prometheus**  | Collects and stores metrics with time-series database; powerful for querying and alerting. |
| **Grafana**     | Visualizes metrics and logs through customizable dashboards; supports real-time monitoring. |
| **Kibana**      | Analyzes and visualizes log data stored in ElasticSearch; ideal for detailed log analytics. |

---

## Objective

- **Bridge academic modeling concepts** to **practical observability** challenges.
- **Apply Linear, Power, Exponential, Logarithmic models** to real microservices monitoring.
- **Help DevOps, SREs, Developers** view their observability setup through the modeling lens.

---

## Actions for Microservices Developers and DevOps Engineers

| Model Type | Developer Actions | DevOps/Observability Actions | Why This Matters |
|------------|--------------------|------------------------------|------------------|
| **Linear** | Identify proportional metrics. | Monitor steady trends and set alerts. | Predictable scaling; simple alerts work. |
| **Power** | Understand performance degradation. | Watch sudden increases in response times. | Detect bottlenecks early. |
| **Exponential** | Recognize cascading failures. | Alert on sudden fast-growing anomalies. | Prevent outages quickly. |
| **Logarithmic** | Recognize flattening gains post-optimization. | Track optimization impact over time. | Manage optimization expectations. |

---

## How to Use HTTP Access Logs and Application Logs for Modeling

| Log Source | Key Fields | Application | Example Usage |
|------------|------------|--------------|---------------|
| **HTTP Access Logs** | `http_response_time`, `http_method`, `http_status_code` | Service latency, error rates, traffic pattern analysis. | Plot response times, error counts, method distributions. |
| **Application Logs** | `timestamp`, `log_level`, `error_stack`, `transaction_id` | Failure patterns, transaction durations. | Calculate durations, plot errors over time. |

---

## Mathematical Functions Using Tool Native Capabilities

| Model Type | Prometheus (PromQL) | Grafana (Visualization) | Kibana (Runtime/Visual Builder) |
|------------|---------------------|--------------------------|---------------------------------|
| **Linear** | `rate(metric_total[5m])`, `increase(metric_total[1h])` | Scale/Offset transform, graph rate. | Derivative aggregation, cumulative sum. |
| **Power** | Emulate using exponent math. | Math expression like `metric ^ 1.5`. | Scripted fields using `Math.pow()`. |
| **Exponential** | `exp(rate(error_total[5m]))` | Exponential moving average smoothing. | Exponential weighted moving averages. |
| **Logarithmic** | `log(rate(metric_total[5m]))` | Logarithmic Y-axis scaling. | Log-transformed scripted fields. |

---

## Why Specific Models Are Recommended Over Others

| Model Type | Why Recommended | Why Others Are Less Preferred |
|------------|------------------|-------------------------------|
| **Linear** | Simple to apply for steady behaviors. | Other models unnecessarily complex. |
| **Exponential** | Best for sudden error spikes. | Too noisy if wrongly used. |
| **Power** | Good for performance under load. | Harder to detect in normal operations. |
| **Logarithmic** | Shows optimization plateaus. | Can distort simple trends. |
| **Logistic** | Advanced: capacity planning. | Complex, not natively supported. |

---

## Native Capabilities vs Custom Ideas

| Tool | Native Capabilities | Custom Creative Uses |
|------|----------------------|----------------------|
| **Kibana** | Time series, log rate analysis, anomaly detection. | Apply linear regression to logs, visualize optimization slowdowns. |
| **Grafana** | Threshold alerts, log Y-axis scaling. | Power visualizations for degradation, exponential smoothing. |
| **Prometheus** | Rate, Increase, Exp, Log functions. | Model system failures with exponential metrics. |

---

## Where My Research Adds Unique Value

This project shows how modeling can **predict system failures**, **improve alerting**, and **optimize monitoring** by:

- Reducing false alarms.
- Detecting real-world non-linear problems.
- Building smarter observability practices.

---

## Key Log Fields for Observability Modeling

| Log Field | Why Important |
|-----------|----------------|
| **HTTP URI** | Identify requested endpoints. |
| **HTTP Method** | Understand operation type. |
| **HTTP Response Time** | Measure latency trends. |
| **HTTP Status Code** | Monitor failures (4xx, 5xx). |
| **Log Level** | Track severity of events. |
| **Transaction ID** | Trace distributed requests. |

---

## Detailed Explanation: Why Some Models Are Less Preferred

| Model Type | What Could Go Wrong | Simple Explanation |
|:-----------|:--------------------|:-------------------|
| **Linear** | Misses critical fast or sudden behaviors in systems with spikes. | Linear models assume steady, predictable changes. They can miss sudden problems. |
| **Exponential** | Triggers too many false alerts if used on stable, slow-changing systems. | Exponential models react very fast. They are noisy if your system is quiet. |
| **Power** | Shows confusing patterns if traffic or load is not strongly changing. | Power models are good under stress/load tests. For normal systems, they exaggerate changes. |
| **Logarithmic** | Makes healthy, normal growth look strange if applied wrongly. | Log scales are useful when improvements slow down. Otherwise they distort normal trends. |
| **Logistic** | Needs manual curve fitting, not available easily in observability tools. | Logistic models are great for capacity planning, not for real-time alerting. |

---

## Acknowledgments

- [Coursera: Fundamentals of Quantitative Modeling](https://www.coursera.org/learn/wharton-quantitative-modeling?specialization=finance-quantitative-modeling-analysts)
- Prometheus, Grafana, Kibana, ElasticSearch open-source communities.

---

