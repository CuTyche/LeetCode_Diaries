# Write your MySQL query statement below
SELECT e.name
FROM Employee as e
INNER JOIN Employee as m
ON e.id = m.managerId
GROUP BY e.id, e.name
HAVING COUNT(m.managerId) >=5;