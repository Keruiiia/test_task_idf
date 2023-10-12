SELECT customers.custmer_name, SUM(transactions.sales_qty) AS total_quantity
FROM transactions
JOIN customers ON transactions.customer_code = customers.customer_code
WHERE transactions.product_code = 'Prod048'
GROUP BY customers.custmer_name
ORDER BY total_quantity DESC
LIMIT 1;
