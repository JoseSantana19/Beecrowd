SELECT name, EXTRACT(DAY FROM payday)::INT as day
FROM loan
