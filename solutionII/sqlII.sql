use bbli354;

GO
IF OBJECT_ID('dbo.AverageCost') IS NOT NULL
DROP PROCEDURE dbo.AverageCost;
GO

CREATE PROCEDURE AverageCost(@target_color varchar(25)) AS
	SELECT AVG(P.StandardCost)
	FROM AdventureWorksLT.SalesLT.Product P
	WHERE P.color = @target_color;
GO

EXEC dbo.AverageCost @target_color = 'Blue';
GO