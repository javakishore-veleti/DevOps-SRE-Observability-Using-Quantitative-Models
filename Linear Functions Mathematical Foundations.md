# Mathematical Foundations of Linear Functions

This guide explains the mathematical basis for **Linear Functions** and how they are applied to real-world DevOps, SRE, and Observability use cases.

---

## Definition

A **Linear Function** is any function that can be written as:

\[
f(x) = a * input_x + b
\]

Where:
- \( a \) = slope (rate of change)
- \( b \) = y-intercept (starting value)
- \( input_x \) = input (independent variable)

In simple words:  
**The output changes at a constant rate relative to the input.**

---

## Behavior

| Parameter | Meaning |
|:----------|:--------|
| \( a > 0 \) | Positive steady growth (upward slope). |
| \( a < 0 \) | Steady decline (downward slope). |
| \( a = 0 \) | No change (constant function). |

In Observability, **linear growth** suggests a system behaving predictably — **each new unit of load causes a fixed increase in resource usage**.

---

## Real-World Observability Examples

| System Metric | Behavior | Model |
|:--------------|:---------|:------|
| CPU Usage vs Incoming Traffic | Steady proportional growth. | Linear Model |
| Memory Usage over Time | Predictable memory consumption rate. | Linear Model |
| HTTP Request Rate Growth | Direct, steady increase over time. | Linear Model |

---

## Graph Shape

- A straight line.
- **Constant slope**: the rate of growth or decline doesn't change.
- Makes it **easy to predict future states** based on past trends.

---

## Key Mathematical Insights

| Feature | Linear Function |
|:--------|:----------------|
| Formula | \( f(x) = a \times x + b \) |
| Application | Predictable and steady system behavior modeling |
| Graph | Straight line (positive or negative slope) |
| Core Use in Observability | Capacity planning, setting simple alert thresholds |

---

## Why This Matters for DevOps and SRE

- **Linear models** are excellent for **early system monitoring** and **capacity planning**.
- When your system metrics grow linearly, **threshold-based alerts** work reliably.
- If metrics start deviating from linearity, it's a **signal for deeper investigation**.

---

## Visual Example (Curve Behavior)

<p align="center">
  <img src="./Visual%20Guide%20-%20Growth%20Shapes.png" alt="Visual Guide - Growth Shapes" width="600"/>
</p>

> *Linear growth appears as a straight diagonal line compared to Power or Exponential curves.*

---

