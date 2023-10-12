SELECT 
    DATE_FORMAT(t.order_date, '%Y-%m') AS month,
    t.product_code AS product,
    SUM(t.sales_qty * t.sales_amount) AS sales
FROM 
    transactions t
WHERE 
    YEAR(t.order_date) = 2020
GROUP BY 
    month, product
ORDER BY 
    month, sales DESC;
