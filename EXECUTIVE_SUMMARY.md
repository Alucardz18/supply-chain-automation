# Executive Summary: Supply Chain Performance Analysis
**DataCo Supply Chain Dataset | 65,752 Orders (180,519 Order Lines) | January 2015 – January 2018**

---

## Overview

This analysis looks at three years of global supply chain operations across five markets
(Europe, LATAM, Pacific Asia, USCA, and Africa). It covers 65,752 orders made up of 180,519
order lines (one line per item), totaling **$36.78M in revenue** and **$3.97M in profit**.
The pipeline was built end to end using Python for automated data cleaning, SQLite for
structured storage, SQL for business analysis, and Power BI for interactive reporting.

The findings show a business with stable revenue for most of the period, held back by poor
delivery performance, and a sharp change in late 2017 where orders became much smaller
and revenue fell.

---

## Key Findings

| Metric | Value |
|---|---|
| Total Orders | 65,752 |
| Total Order Lines | 180,519 |
| Total Revenue | $36.78M |
| Total Profit | $3.97M |
| Overall Profit Margin | 10.8% |
| Late Delivery Rate | **54.8%** of orders |
| First Class Late Rate | **95.3%** |
| Top Market by Revenue | Europe ($10.9M) |
| Top Category by Profit | Fishing ($756K) |

---

## Critical Issues

### 1. Most Orders Arrive Late
**54.8%** of orders arrive late (57.3% if cancelled orders are left out). The rate is almost
the same in every market, between 54.1% and 55.3%, so this is not a regional problem. Late
deliveries hurt customer trust, raise support costs, and put repeat purchases at risk.

The worst result is in **First Class, the premium tier, with a 95.3% late rate**. First Class
is always scheduled for 1-day delivery, so almost any order that takes 2 days or more counts
as late. Either the 1-day promise is unrealistic or First Class orders are not being shipped
fast enough. In both cases, the customers who pay more for faster shipping get the worst
experience.

### 2. The Late 2017 Change in Orders
From January 2015 to September 2017, the business averaged about 1,740 orders and 11,400
items sold per month, with each order containing several items. Starting in **October 2017**,
almost every order contains just 1 item. The number of orders stayed about the same (around
2,050 to 2,100 per month), but items sold fell to about 2,100 per month. The number of
different products sold each month also dropped, from between 42 and 87 before October to
between 8 and 20 after.

Revenue followed with a short delay: it was still $1.07M in October 2017, then fell to $627K
in November and $332K by January 2018. Customers kept placing orders, but they bought much
less per order, which points to a shrinking product range rather than lost customers.

---

## What I Would Do Differently

### Fix 1: Investigate First Class delivery times
A 95.3% late rate on the premium tier means the 1-day promise is almost never met. I would
compare actual and scheduled shipping days for First Class orders by warehouse, region, and
carrier to find where the extra time comes from. Then I would either fix the process so
1-day delivery is realistic, or change the promise to match what can be delivered. Until
then, I would pause First Class upsell messaging to avoid disappointing more customers.

### Fix 2: Review shipping performance across all tiers
Standard Class has the lowest late rate at 38.1%, but it also allows the most time (4 days).
That means part of the gap between tiers comes from how much time each tier allows, not only
from how well orders are shipped. I would track actual shipping days for every tier, set
clear targets for each one, and review carrier contracts where targets are missed. The goal
is to bring the overall late delivery rate below 20% within two quarters.

### Fix 3: Grow order size in Pacific Asia
Pacific Asia is the third largest market by revenue ($8.3M) but the second largest by number
of orders (17,577), ahead of LATAM. Its customers order often but spend less per order. I
would focus on raising order value there through bundles, higher value products, and
targeted promotions, since the demand is already in place.

### Fix 4: Use Fishing to lift other outdoor categories
Fishing generates $756K in profit, 19% of total company profit from a single category. I
would use it as a cross-sell anchor for other outdoor categories, such as Camping & Hiking
(already the third most profitable at $427K) and Hunting & Shooting, which ranks 31st out of
50 categories. Bundles, product recommendations, and targeted promotions could turn Fishing's
demand into larger baskets across the outdoor range.

### Fix 5: Investigate the late 2017 drop in products and basket size
A change this sudden, from several items per order to 1 within a single month, is consistent
with an internal disruption: a product range cut, a supplier failure, stock shortages, or a
change in how orders were recorded. I would check product availability, supplier deliveries,
and inventory levels for September and October 2017 to find the cause. If it was a supply
problem, the priority is building backups (more suppliers, spread out warehouse stock, and
automatic low stock alerts) so it cannot happen again at this scale.

---

## Summary

This business has a strong foundation: stable revenue for almost three years, customers in
five markets, and clear category winners. However, more than half of its orders arrive late,
and it has not yet explained why orders shrank to a single item in late 2017.

The immediate priority is delivery reliability. The medium term opportunities are growing
order size in Pacific Asia and cross-selling around the Fishing category. The open question
of what changed in October 2017 is the most important investigation to complete before
making any further growth commitments.

---
