# Write your MySQL query statement below
With OrderCount as (
    SELECT customer_number, COUNT(order_number) as ord
    FROM Orders 
    GROUP BY customer_number
)
SELECT customer_number
FROM OrderCount
WHERE ord = (SELECT MAX(ord) FROM OrderCount);







-- SELECT customer_number
-- FROM (
--     SELECT customer_number, COUNT(order_number) as ord
--     FROM Orders 
--     GROUP BY customer_number
-- ) AS subquery
-- WHERE ord = (
--     SELECT MAX(ord) 
--     FROM (
--         SELECT customer_number, COUNT(order_number) as ord
--     FROM Orders 
--     GROUP BY customer_number) 
--     AS max_subquery 
-- );

