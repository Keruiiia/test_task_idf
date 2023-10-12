SELECT SUM(transactions.sales_amount) AS total_revenue
FROM transactions
JOIN date ON transactions.order_date = date.date
WHERE YEAR(date.cy_date) = 2020 AND MONTH(date.cy_date) = 1;