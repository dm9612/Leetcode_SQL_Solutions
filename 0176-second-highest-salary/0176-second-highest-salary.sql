# Write your MySQL query statement below

-- SELECT MAX(salary) as SecondHighestSalary
-- FROM Employee
-- WHERE salary < (SELECT MAX(salary) FROM Employee);

SELECT (
    SELECT distinct salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1) as SecondHighestSalary;