SELECT temperature, count(*)
FROM records
GROUP BY temperature,mark
ORDER BY mark ASC
