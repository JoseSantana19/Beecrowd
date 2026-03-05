SELECT amount
FROM value_table
GROUP BY amount
ORDER BY count(*) DESC
LIMIT 1
