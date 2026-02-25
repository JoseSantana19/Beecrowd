SELECT prod.name, prov.name, cat.name
FROM providers prov
INNER JOIN products prod
ON prov.id = prod.id_providers
INNER JOIN categories cat
ON prod.id_categories = cat.id
WHERE prov.name = 'Sansul SA' AND cat.name = 'Imported'
