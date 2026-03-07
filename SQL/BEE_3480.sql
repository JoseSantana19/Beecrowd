WITH cte as (
  SELECT
  	queue,
  	LAG(id) OVER (PARTITION BY queue ORDER BY id ASC) AS left_id,
  	id AS right_id,
  	LAG(available) OVER (PARTITION BY queue ORDER BY id ASC) AS left_available,
  	available AS right_available
  FROM chairs
)
SELECT
  queue,
  left_id as left,
  right_id as right
FROM cte
WHERE left_available AND right_available
