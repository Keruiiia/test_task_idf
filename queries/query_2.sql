SELECT
    SUM(sales_amount) as total_revenue
FROM
    transactions
WHERE
    YEAR(order_date) = 2020 AND MONTH(order_date) = 1;
