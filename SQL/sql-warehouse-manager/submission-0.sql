-- Write your query below
SELECT 
    w.name AS warehouse_name, 
    SUM(COALESCE(p.width, 0) * COALESCE(p.length, 0) * COALESCE(p.height, 0) * COALESCE(w.units, 0)) AS volume
FROM warehouse w LEFT JOIN products p
ON w.product_id = p.product_id
GROUP BY w.name