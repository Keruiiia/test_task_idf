SELECT
    date.month_name, AVG(transactions.sales_qty) AS average_quantity
FROM
    transactions
    JOIN date ON transactions.order_date = date.date
GROUP BY
    date.month_name;
