WITH primeiro_time AS (
	SELECT
  	team_1 AS team_id,
  	CASE WHEN team_1_goals > team_2_goals then 1 else 0 END AS victories,
  	CASE WHEN team_1_goals < team_2_goals then 1 else 0 END AS defeats,
  	CASE WHEN team_1_goals = team_2_goals then 1 else 0 END AS draws,
  	CASE
  		WHEN team_1_goals > team_2_goals THEN 3
  		WHEN team_1_goals = team_2_goals THEN 1
  		WHEN team_1_goals < team_2_goals THEN 0
  	END AS score
  FROM matches
),
segundo_time AS (
  SELECT
  	team_2 AS team_id,
  	CASE WHEN team_2_goals > team_1_goals then 1 else 0 END AS victories,
  	CASE WHEN team_2_goals < team_1_goals then 1 else 0 END AS defeats,
  	CASE WHEN team_2_goals = team_1_goals then 1 else 0 END AS draws,
  	CASE
  		WHEN team_2_goals > team_1_goals THEN 3
  		WHEN team_2_goals = team_1_goals THEN 1
  		WHEN team_2_goals < team_1_goals THEN 0
  	END AS score
  	FROM matches
)
SELECT
  name,
  count(*) as matches,
  sum(victories) AS victories,
  sum(defeats) AS defeats,
  sum(draws) as draws,
  sum(score) AS score
FROM (SELECT * FROM primeiro_time UNION ALL SELECT * FROM segundo_time) a
LEFT JOIN teams b
ON a.team_id = b.id
GROUP BY name
ORDER BY score DESC
