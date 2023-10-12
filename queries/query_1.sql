SELECT SUM(transactions.sales_amount) AS total_revenue
FROM transactions
JOIN markets ON transactions.market_code = markets.markets_code
JOIN date ON transactions.order_date = date.date
WHERE YEAR(date.cy_date) = 2020 AND markets.markets_name = 'Chennai';
