SELECT DISTINCT a.node_id,
  CASE
   WHEN a.pointer IS NULL THEN 'LEAF'
   WHEN (SELECT COUNT(b.pointer) FROM nodes b WHERE b.pointer = a.node_id) = 0 THEN 'ROOT'
   ELSE 'INNER'
  END as type
FROM nodes a;
