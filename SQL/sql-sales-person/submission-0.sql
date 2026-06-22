-- Write your query below
WITH order_with_com_name AS (
    SELECT o.sales_id, o.order_id, c.name 
    FROM orders o INNER JOIN company c 
    ON o.com_id = c.com_id
    WHERE c.name = 'CRIMSON'
)

SELECT p.name
FROM sales_person p LEFT JOIN order_with_com_name oc
ON p.sales_id = oc.sales_id
WHERE oc.order_id IS NULL;