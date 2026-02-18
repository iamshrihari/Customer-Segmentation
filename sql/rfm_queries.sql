-- RFM Table Query
SELECT 
    CustomerID,
    MAX(InvoiceDate) AS LastPurchaseDate,
    COUNT(DISTINCT InvoiceNo) AS Frequency,
    SUM(Quantity * UnitPrice) AS Monetary
FROM sales
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID;
