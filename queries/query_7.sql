SELECT
    date.cy_date as month,
    transactions.product_code as product,
    SUM(transactions.sales_qty * transactions.sales_amount) as sales
FROM
    transactions
JOIN date ON transactions.order_date = date.date
WHERE
    date.year = 2020
GROUP BY
    date.cy_date, transactions.product_code
ORDER BY
    product, month;
