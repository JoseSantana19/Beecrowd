SELECT p.id, p.name
FROM products p
INNER JOIN categories c
ON p.id_categories = c.id
AND c.name LIKE 'super%'
