-- Write your query below
SELECT p.name
FROM sales_person p
WHERE NOT EXISTS (
    SELECT 1 
    FROM orders o 
    INNER JOIN company c ON o.com_id = c.com_id
    WHERE o.sales_id = p.sales_id 
    AND c.name = 'CRIMSON'
);