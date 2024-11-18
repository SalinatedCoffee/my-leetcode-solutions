SELECT eu.unique_id, em.name
-- row in Employees may not have corresponding row in EmployeeUNI
-- we want to include such employees in the query, so perform OUTER JOIN
FROM Employees em LEFT OUTER JOIN EmployeeUNI eu
    ON eu.id = em.id;

