# Write your MySQL query statement below
SELECT Visits.customer_id, count(Visits.customer_id) as count_no_trans
FROM Visits
LEFT JOIN Transactions
ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.Visit_id IS NULL
GROUP BY Visits.customer_id;