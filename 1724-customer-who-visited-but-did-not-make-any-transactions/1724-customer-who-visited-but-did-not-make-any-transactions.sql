# Write your MySQL query statement below

SELECT v.customer_id, COUNT(*) as count_no_trans
FROM Visits v
LEFT JOIN Transactions t 
on v.visit_id = t.visit_id
WHERE transaction_id is NULL
GROUP BY customer_id;

-- With cte as(
--     SELECT v.visit_id, v.customer_id, t.transaction_id, t.amount
--     FROM Visits v
--     LEFT JOIN Transactions t 
--     on v.visit_id = t.visit_id
-- )
-- SELECT customer_id , COUNT(customer_id) as count_no_trans
-- FROM cte
-- WHERE transaction_id is NULL
-- GROUP BY customer_id;

