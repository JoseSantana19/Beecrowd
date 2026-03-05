SELECT name, SUM(salary) AS salary
FROM (
  SELECT d.name, ROUND(150 * (1+(ws.bonus/100.0)) * a.hours,1) as salary
  FROM attendances a
  LEFT JOIN work_shifts ws
  ON a.id_work_shift = ws.id
  LEFT JOIN doctors d
  ON a.id_doctor = d.id
) tabela
GROUP BY name
ORDER BY salary DESC
