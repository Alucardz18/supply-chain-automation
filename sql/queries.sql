-- Query 1: Delivery Delay Rate by Shipping Mode
SELECT 
    "Shipping Mode",
    count(*) AS total_orders,
    sum("Late_delivery_risk") AS late_deliveries,
    round(sum(Late_delivery_risk) * 100.0 / count(*), 2) AS delivery_delay_rate
FROM cleaned_supply_chain
GROUP BY "Shipping Mode"
ORDER BY delivery_delay_rate DESC;

-- Query 2: Revenue by Market
SELECT
    "Market",
    round(sum("Sales"), 2) as total_sales,
    round(sum("Order Profit Per Order"), 2) as total_profit,
    count(*) as total_orders
FROM cleaned_supply_chain   
GROUP BY "Market"
ORDER BY total_sales DESC;

-- Query 3: Top 5 Most Profitable Categories
SELECT
    "Category Name",
    round(sum("Order Profit Per Order"), 2) as total_profit,
    count(*) as total_orders
FROM cleaned_supply_chain
GROUP BY "Category Name"
ORDER BY total_profit DESC
LIMIT 5;

-- Query 4: Monthly Order Trends
SELECT  
    strftime('%Y-%m', "order date (DateOrders)") AS order_month,
    count(*) AS total_orders,
    round(sum("Sales"), 2) AS total_sales,
    round(sum("Order Profit Per Order"), 2) AS total_profit
FROM cleaned_supply_chain
GROUP BY order_month
ORDER BY order_month;