-- Write your query below
SELECT *
FROM customers
WHERE customer_id NOT IN
(
    SELECT customer_id
    FROM orders
    WHERE product_name = 'C'
)
AND customer_id IN
(
    SELECT customer_id
    FROM orders
    WHERE product_name = 'A'
)
AND customer_id IN
(
    SELECT customer_id
    FROM orders
    WHERE product_name = 'B'
)
ORDER BY customer_name;