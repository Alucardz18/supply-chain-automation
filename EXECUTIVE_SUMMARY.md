# Executive Summary — Supply Chain Performance Analysis
**DataCo Supply Chain Dataset | 180,519 Orders | January 2015 – January 2018**

---

## Overview

This analysis examines three years of global supply chain operations across five markets —
Europe, LATAM, Pacific Asia, USCA, and Africa — covering 180,519 orders totaling **$36.78M
in revenue** and **$3.97M in profit**. The pipeline was built end-to-end using Python for
automated data cleaning, SQLite for structured storage, SQL for business analysis, and Power
BI for interactive reporting.

The findings reveal a business with strong and stable revenue fundamentals undermined by a
systemic delivery performance crisis — and a sharp, unexplained operational decline in Q4 2017
that demands urgent investigation.

---

## Key Findings

| Metric | Value |
|---|---|
| Total Orders | 180,519 |
| Total Revenue | $36.78M |
| Total Profit | $3.97M |
| Overall Profit Margin | 10.8% |
| Late Delivery Rate | **54.8%** |
| First Class Late Rate | **95.3%** |
| Top Market by Revenue | Europe ($10.9M) |
| Top Category by Profit | Fishing ($756K) |

---

## Critical Issues

### 1. Delivery Performance is a Business Emergency
Over half of all orders — **54.8%** — arrive late. This is not a marginal inefficiency;
it is a structural failure that touches every market, every product category, and every
customer segment. Late deliveries erode customer trust, increase support costs, and
threaten repeat purchase rates.

More critically, **First Class shipping — the premium tier — has a 95.3% late delivery
rate**. Customers who pay more for faster service are paradoxically receiving the worst
outcomes. This creates a dangerous inversion: the company is actively disappointing its
highest-value customers at the moment they signal the most trust.

### 2. The October 2017 Decline
Order volume dropped from approximately 5,300 orders per month to under 2,300 after
October 2017 — a decline of more than 50% in two months. Revenue followed, falling from
a peak of ~$1.1M monthly to $331K by January 2018. This pattern is too sharp and
sustained to be seasonal and warrants immediate root cause analysis.

---

## What I Would Do Differently

### Fix 1 — Investigate the carrier and route behind First Class delays
A 95.3% late delivery rate on a premium shipping tier is not a random distribution problem
— it points to a specific carrier contract, routing inefficiency, or warehouse processing
failure. I would pull shipment-level data, map delay clusters by origin warehouse and
destination region, and identify whether this is a single carrier failing or a systemic
routing issue. Until the root cause is confirmed, I would pause First Class upsell
messaging to avoid compounding customer disappointment.

### Fix 2 — Switch to better-performing carriers across all tiers
Standard Class, despite being the cheapest option, has the lowest late delivery rate at
38.1%. This confirms the problem is not volume or geography — it is carrier-specific
execution. I would conduct a carrier performance audit across all shipping modes, establish
SLA benchmarks, and renegotiate or replace contracts with underperforming logistics
partners. The goal is to bring the overall late delivery rate below 20% within two quarters.

### Fix 3 — Prioritize Pacific Asia for growth investment
Europe is the top revenue market at $10.9M and is already well-penetrated. Rather than
over-investing in a mature market, I would redirect growth capital toward **Pacific Asia**,
which represents the second-largest and fastest-growing market at $8.3M and 41,260 orders.
The region has demonstrated demand without proportional marketing investment — meaning
marginal spend here likely yields higher returns than in Europe.

### Fix 4 — Bundle Fishing products with underperforming categories
Fishing generates $756K in profit — 19% of total company profit from a single category.
Rather than simply expanding the line in isolation, I would use it as a cross-sell vehicle.
Customers purchasing fishing equipment represent an outdoor lifestyle segment with adjacent
interests in Camping & Hiking, Footwear, and Outdoors — all of which currently
underperform. Bundling, recommendation algorithms, and targeted promotions would transfer
Fishing's demand signal into adjacent categories and lift overall basket size.

### Fix 5 — Investigate the Q4 2017 decline as an internal supply chain disruption
A drop this sharp — 50%+ in under 60 days — is consistent with an internal disruption:
a key supplier failure, a warehouse system outage, a logistics partner collapse, or an
inventory shortfall. I would cross-reference the decline with warehouse throughput data,
supplier delivery logs, and customer cancellation records to isolate the origin. If this
was a preventable internal failure, the priority is building redundancy — backup suppliers,
distributed warehouse capacity, and automated low-stock alerts — to ensure it cannot
recur at the same scale.

---

## Summary

This business has a strong foundation: stable multi-year revenue, a globally distributed
customer base, and clear category winners. However, it is losing customer confidence
through broken delivery promises and has not yet diagnosed what caused its most significant
operational collapse in the dataset period.

The immediate priority is delivery reliability. The medium-term opportunity is Pacific Asia
expansion and cross-category bundling anchored to the Fishing category's proven demand.
The unresolved question — what happened in October 2017 — is the single most important
investigation this business needs to complete before making any further growth commitments.

---

*Analysis conducted using Python (pandas, SQLAlchemy), SQLite, and Power BI.
Source: DataCo Smart Supply Chain Dataset — 180,519 orders across 50 variables.*