-- SUPERSTORE ANALYSIS QUERIES
-- Table: superstore

-- 1. View full dataset
SELECT * 
FROM python_db.superstore;

-- 2. Top-selling category in each region
SELECT Region, Category, SUM(Sales) AS total_sales
FROM superstore
GROUP BY Region, Category
ORDER BY Region, total_sales DESC;

-- 3. Which region generates the most revenue?
SELECT Region, SUM(Sales) AS total_sales
FROM superstore
GROUP BY Region
ORDER BY total_sales DESC;

-- 4. Category-wise performance
SELECT Category, SUM(Sales) AS total_sales
FROM superstore
GROUP BY Category
ORDER BY total_sales DESC;

-- 5. States with losses
SELECT State, SUM(Profit) AS total_profit
FROM superstore
GROUP BY State
HAVING total_profit < 0
ORDER BY total_profit;

-- 6. Top 10 customers by sales
SELECT `Customer Name`, SUM(Sales) AS total_sales
FROM superstore
GROUP BY `Customer Name`
ORDER BY total_sales DESC
LIMIT 10;

-- 7. Which shipping mode is most profitable?
SELECT `Ship Mode`, ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct
FROM superstore
GROUP BY `Ship Mode`
ORDER BY profit_margin_pct DESC;

-- 8.Monthly sales trend
SELECT DATE_FORMAT(`Order Date`, '%Y-%m') AS order_month,
       SUM(Sales) AS monthly_sales
FROM superstore
GROUP BY order_month
ORDER BY order_month;
