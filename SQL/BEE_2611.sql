SELECT m.id, name
FROM movies m
LEFT JOIN genres g
ON m.id_genres = g.id
WHERE g.description = 'Action'
