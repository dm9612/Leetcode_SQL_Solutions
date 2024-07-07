# Write your MySQL query statement below
SELECT name as Customers
FROM Customers c 
LEFT JOIN Orders o
on o.customerId = c.id
WHERE o.customerId is Null