SELECT SUBSTRING(np.cpf,1,3) || '.' ||
    SUBSTRING(np.cpf,4,3) || '.' ||
    SUBSTRING(np.cpf,7,3) || '-' ||
    SUBSTRING(np.cpf,10,2)
    AS CPF
FROM customers c
INNER JOIN natural_person np
ON c.id = np.id_customers
