SELECT customers.custmer_name, SUM(transactions.sales_qty) AS total_purchases
FROM transactions
JOIN customers ON transactions.customer_code = customers.customer_code
JOIN date ON transactions.order_date = date.date
WHERE YEAR(date.cy_date) = 2017
GROUP BY customers.custmer_name
ORDER BY total_purchases DESC
LIMIT 10;
