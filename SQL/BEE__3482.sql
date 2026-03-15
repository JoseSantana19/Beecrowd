WITH cte AS (
SELECT
  u1.user_id,
	u1.user_name AS usuario,
	u1.posts AS posts_usuario,
	u2.user_name AS seguidor,
	u2.posts AS posts_seguidor
FROM followers f
LEFT JOIN users u1
	ON f.user_id_fk = u1.user_id
LEFT JOIN users u2
	ON f.following_user_id_fk = u2.user_id
)
SELECT 
  usuario AS u1_name,
  seguidor AS u2_name
FROM cte t1
WHERE posts_usuario < posts_seguidor AND EXISTS (
  SELECT *
  FROM cte t2
  WHERE t2.posts_usuario = t1.posts_seguidor AND t2.posts_seguidor = t1.posts_usuario
)
ORDER BY user_id
