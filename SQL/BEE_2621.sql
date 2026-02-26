SELECT prod.name
FROM providers prov
INNER JOIN products prod
ON prov.id = prod.id_providers
WHERE prod.amount >= 10
    AND prod.amount <= 20
    AND prov.name LIKE 'P%'
