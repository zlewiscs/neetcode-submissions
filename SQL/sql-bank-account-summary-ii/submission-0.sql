-- Write your query below
WITH total_balance AS (
    SELECT account, SUM(amount) AS balance
    FROM transactions
    GROUP BY account
)

SELECT u.name, tb.balance
FROM users u INNER JOIN total_balance tb
ON u.account = tb.account
WHERE tb.balance > 10000