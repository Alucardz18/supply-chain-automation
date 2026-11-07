-- Query 1: Late delivery rate by shipping mode (per order)
SELECT
    "Shipping Mode",
    count(DISTINCT "Order Id") AS total_orders,
    count(DISTINCT CASE WHEN "Late_delivery_risk" = 1 THEN "Order Id" END) AS late_orders,
    round(count(DISTINCT CASE WHEN "Late_delivery_risk" = 1 THEN "Order Id" END) * 100.0
          / count(DISTINCT "Order Id"), 2) AS delivery_delay_rate
FROM cleaned_supply_chain
GROUP BY "Shipping Mode"
ORDER BY delivery_delay_rate DESC;

-- Query 2: Sales, profit, orders and order lines by market
SELECT
    "Market",
    round(sum("Sales"), 2) AS total_sales,
    round(sum("Order Profit Per Order"), 2) AS total_profit,
    count(DISTINCT "Order Id") AS total_orders,
    count(*) AS order_lines
FROM cleaned_supply_chain
GROUP BY "Market"
ORDER BY total_sales DESC;

-- Query 3: Top 5 categories by profit
SELECT
    "Category Name",
    round(sum("Order Profit Per Order"), 2) AS total_profit,
    count(DISTINCT "Order Id") AS total_orders
FROM cleaned_supply_chain
GROUP BY "Category Name"
ORDER BY total_profit DESC
LIMIT 5;

-- Query 4: Orders, items sold, sales and profit per month
SELECT
    strftime('%Y-%m', "order date (DateOrders)") AS order_month,
    count(DISTINCT "Order Id") AS total_orders,
    sum("Order Item Quantity") AS items_sold,
    round(sum("Sales"), 2) AS total_sales,
    round(sum("Order Profit Per Order"), 2) AS total_profit
FROM cleaned_supply_chain
GROUP BY order_month
ORDER BY order_month;
