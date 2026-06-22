-- Write your query below
WITH pre_join_distance_sum AS (
    SELECT user_id, SUM(distance) AS travelled_distance
    FROM rides
    GROUP BY user_id
)

SELECT u.name, COALESCE(ps.travelled_distance, 0) AS travelled_distance
FROM users u LEFT JOIN pre_join_distance_sum ps
ON u.id = ps.user_id
ORDER BY COALESCE(ps.travelled_distance, 0) DESC, u.name;