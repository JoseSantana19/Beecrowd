SELECT a.name, b.name
FROM products a
LEFT JOIN providers b
ON a.id_providers = b.id
WHERE id_categories = 6
