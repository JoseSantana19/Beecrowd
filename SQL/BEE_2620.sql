SELECT c.name, o.id
FROM customers c
INNER JOIN orders o
ON c.id = o.id_customers
WHERE LEFT(CAST(orders_date AS TEXT),7) >= '2016-01'
    AND LEFT(CAST(orders_date AS TEXT),7) <= '2016-06'
