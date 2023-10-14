SELECT
    SUM(sales_amount) as total_revenue
FROM
    transactions
    JOIN markets ON transactions.market_code = markets.markets_code
WHERE
    YEAR(order_date) = 2020 AND markets_name = 'Chennai';

