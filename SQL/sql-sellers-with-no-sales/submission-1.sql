-- Write your query below
SELECT s.seller_name
FROM seller s
WHERE s.seller_id NOT IN (
    SELECT DISTINCT seller_id
    FROM orders
    WHERE sale_date >= '2020-01-01' AND sale_date < '2021-01-01'
)
ORDER BY s.seller_name;