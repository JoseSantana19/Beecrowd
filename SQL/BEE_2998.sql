WITH cte AS (
    SELECT 
    	c.name,
    	c.investment,
    	o.month,
    	o.profit,
    	SUM(profit) OVER(PARTITION BY c.name ORDER BY o.month ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as profit_acumulado
    FROM operations o
    LEFT JOIN clients c
    ON o.client_id = c.id
)
SELECT name,
  MIN(investment),
  MIN(month) AS month_of_payback,
  MIN(profit_acumulado) - MIN(investment) AS return
FROM cte
WHERE profit_acumulado >= investment
GROUP BY name
ORDER BY return DESC
