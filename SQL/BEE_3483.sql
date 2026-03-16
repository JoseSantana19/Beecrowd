WITH tabela AS(
  SELECT *
    FROM cities
    WHERE population NOT IN (
      (
      SELECT MAX(population)
      FROM cities
      ),
      (
      SELECT MIN(population)
      FROM cities
      )
    )
)
SELECT city_name, population
FROM tabela
WHERE population IN (
  (
  SELECT MAX(population)
  FROM tabela
  ),
  (
  SELECT MIN(population)
  FROM tabela
  )
)
