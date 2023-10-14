SELECT
    customers.custmer_name, SUM(transactions.sales_qty) as total_quantity
FROM
    transactions
    JOIN customers ON transactions.customer_code = customers.customer_code
WHERE
    YEAR(transactions.order_date) = 2017
GROUP BY
    customers.custmer_name
ORDER BY
    total_quantity DESC
LIMIT 10;

