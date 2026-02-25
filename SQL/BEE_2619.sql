SELECT prod.name, prov.name, prod.price
FROM providers prov
INNER JOIN products prod
ON prov.id = prod.id_providers
INNER JOIN categories cat
ON prod.id_categories = cat.id
WHERE prod.price > 1000 AND cat.name = 'Super Luxury'
