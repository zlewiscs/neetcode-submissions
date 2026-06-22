-- Write your query below
WITH total_balance_over_tenk AS (
    SELECT account, SUM(amount) AS balance
    FROM transactions
    GROUP BY account
    HAVING sum(amount) > 10000
)

SELECT u.name, tb.balance
FROM users u INNER JOIN total_balance_over_tenk tb
ON u.account = tb.account