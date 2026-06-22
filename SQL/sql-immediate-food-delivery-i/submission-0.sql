-- Write your query below
WITH instant_delivery_label AS (
    SELECT
        d.*,
        CASE
            WHEN d.order_date = d.customer_pref_delivery_date THEN 1
            ELSE 0
        END AS is_instant_delivery
    FROM delivery d
)

SELECT 
    ROUND(
        ((SUM(is_instant_delivery) / CAST(COUNT(delivery_id) AS FLOAT)) * 100)::numeric
        , 2
    ) AS immediate_percentage
FROM instant_delivery_label