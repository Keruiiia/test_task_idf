SELECT markets.markets_name, SUM(transactions.sales_amount) AS total_sales_amount
FROM transactions
JOIN markets ON transactions.market_code = markets.markets_code
GROUP BY markets.markets_name
ORDER BY total_sales_amount DESC;
