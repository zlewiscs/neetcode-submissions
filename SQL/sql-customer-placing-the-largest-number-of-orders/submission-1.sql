-- Write your query below
WITH order_count AS (
    SELECT customer_number, COUNT(order_number) AS total_order_count
    FROM orders
    GROUP BY customer_number
)

SELECT customer_number
FROM order_count
WHERE total_order_count = (
        SELECT MAX(total_order_count) FROM order_count
    )
;