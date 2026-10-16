
-- 1. Display all sales records
SELECT *
FROM sales;

-- 2. Display all customers
SELECT *
FROM customers;

-- 3. Display all products
SELECT *
FROM products;

-- 4. Calculate revenue for each sale
SELECT
    order_id,
    product_id,
    quantity,
    unit_price,
    quantity * unit_price AS revenue
FROM sales
JOIN products
    ON sales.product_id = products.product_id;

-- 5. Calculate total revenue by region
SELECT
    customers.region,
    SUM(sales.quantity * products.unit_price) AS total_revenue
FROM sales
LEFT JOIN customers
    ON sales.customer_id = customers.customer_id
LEFT JOIN products
    ON sales.product_id = products.product_id
GROUP BY customers.region;
