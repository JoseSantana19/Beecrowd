SELECT c.name, r.rentals_date
FROM customers c
LEFT JOIN rentals r
ON c.id = r.id_customers
WHERE LEFT(r.rentals_date::TEXT,7) = '2016-09'
