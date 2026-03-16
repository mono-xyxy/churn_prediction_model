SELECT 
strftime('%Y-%m', order_purchase_timestamp) AS month,
SUM(payment_value) AS monthly_revenue
FROM orders
JOIN order_payments
ON orders.order_id = order_payments.order_id
GROUP BY month
ORDER BY month;

SELECT 
product_category_name,
SUM(price) AS revenue
FROM order_items
JOIN products
ON order_items.product_id = products.product_id
GROUP BY product_category_name
ORDER BY revenue DESC
LIMIT 10;

SELECT 
customer_state,
AVG(
julianday(order_delivered_customer_date) -
julianday(order_purchase_timestamp)
) AS avg_delivery_days
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
GROUP BY customer_state
ORDER BY avg_delivery_days DESC;