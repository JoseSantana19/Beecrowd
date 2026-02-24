SELECT c.name, sum(p.amount)
FROM products p
LEFT JOIN categories c
ON p.id_categories = c.id
GROUP BY c.name
