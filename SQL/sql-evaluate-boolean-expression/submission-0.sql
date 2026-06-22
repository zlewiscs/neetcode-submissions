-- Write your query below
SELECT 
    e.*,
    CASE
        WHEN operator = '<' AND lv.value < rv.value THEN TRUE
        WHEN operator = '=' AND lv.value = rv.value THEN TRUE
        WHEN operator = '>' AND lv.value > rv.value THEN TRUE
        ELSE FALSE
    END AS value
FROM variables lv INNER JOIN expressions e 
ON lv.name = e.left_operand
INNER JOIN variables rv
ON rv.name = e.right_operand
    