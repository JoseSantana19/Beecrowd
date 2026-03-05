SELECT e.cpf, e.enome, d.dnome
FROM empregados e
LEFT JOIN departamentos d
ON e.dnumero = d.dnumero
LEFT JOIN trabalha t
ON CAST(e.cpf AS BIGINT) = CAST(t.cpf_emp AS BIGINT)
WHERE t.cpf_emp isnull
ORDER BY e.cpf
