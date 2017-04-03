SELECT C.CustomerID
FROM 
AdventureWorksLT.SalesLT.Customer C,
AdventureWorksLT.SalesLT.SalesOrderHeader H,
AdventureWorksLT.SalesLT.SalesOrderDetail D,
AdventureWorksLT.SalesLT.Product P
WHERE
C.CustomerID = H.CustomerID AND H.SalesOrderID = D.SalesOrderID AND D.ProductID = P.ProductID AND P.Color = 'red'
ORDER BY C.CustomerID;
GO

IF OBJECT_ID('dbo.RedSpending','v') IS NOT NULL 
DROP VIEW dbo.RedSpending;
GO

CREATE VIEW RedSpending AS
SELECT C.CustomerID, C.FirstName, C.LastName, MAX(D.UnitPrice) AS HighestPrice
FROM 
AdventureWorksLT.SalesLT.Customer C,
AdventureWorksLT.SalesLT.SalesOrderHeader H,
AdventureWorksLT.SalesLT.SalesOrderDetail D,
AdventureWorksLT.SalesLT.Product P
WHERE
C.CustomerID = H.CustomerID AND H.SalesOrderID = D.SalesOrderID AND D.ProductID = P.ProductID AND P.Color = 'red'
GROUP BY C.CustomerID, C.FirstName, C.LastName;
