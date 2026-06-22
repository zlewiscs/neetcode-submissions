-- Write your query below
SELECT a.sale_date, (a.sold_num - o.sold_num) AS diff
FROM sales a INNER JOIN sales o
ON a.sale_date = o.sale_date 
    AND a.fruit = 'apples' 
    AND o.fruit = 'oranges'