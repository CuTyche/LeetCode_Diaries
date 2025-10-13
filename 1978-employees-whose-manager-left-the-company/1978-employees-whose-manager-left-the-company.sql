# Write your MySQL query statement below

WITH employee_cte AS(
    SELECT e.employee_id as e_id,
    e.salary as salary,
    e.manager_id as m_id1,
    m.employee_id as m_id2
    FROM Employees e
    LEFT JOIN Employees m
    ON e.manager_id = m.employee_id
)

SELECT 
e_id as employee_id
FROM employee_cte
WHERE salary < 30000 and m_id1 IS NOT NULL and m_id2 IS NULL
ORDER BY e_id;