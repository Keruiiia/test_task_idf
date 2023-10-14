SELECT
    date.month_name AS month,
    transactions.product_code as product,
    SUM(transactions.sales_qty * transactions.sales_amount) as sales
FROM
    transactions
    JOIN date ON transactions.order_date = date.date
WHERE
    date.year = 2020
GROUP BY
    date.month_name, transactions.product_code
ORDER BY
    month;
