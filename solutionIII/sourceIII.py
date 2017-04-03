# CMPT354 - A3 - Part B - Part III
# Author: Bei Bei Li - 301254625

#import the library for the database interface
import pymssql
#connect to
connection = pymssql.connect(host='cypress.csil.sfu.ca', user='s_bbli', password='3trrbAjmTjMde4P3', database='bbli354')

#set cursor
cursor = connection.cursor()

#display colors of products excluding NULL, sorted in alphbetical order
print "All and only colors of products in the Product table in alphabetical order, including Multi but excluding NULL: "
myquery = "SELECT DISTINCT P.Color FROM AdventureWorksLT.SalesLT.Product P WHERE P.Color IS NOT NULL ORDER BY P.Color;"
cursor.execute(myquery)
result = cursor.fetchone()
while result:
    out = "Color: " + str(result[0])
    print out
    result = cursor.fetchone()

print

#accept a single string input
color = raw_input("please select a color name from the above list: ")
print

#create view table for that color input
if ((color == "Silver/Black") or (color == "silver/black") or  (color == "Silver/black") or (color == "silver/Black")):
    viewname = 'SilverBlackSpending'
else:
    viewname = color + 'Spending'
check = "IF OBJECT_ID('dbo." + viewname + "','v') IS NOT NULL DROP VIEW dbo." + viewname + ";"
cursor.execute(check)

myquery2 = "CREATE VIEW " + viewname + " AS SELECT C.CustomerID, C.FirstName, C.LastName, MAX(D.UnitPrice) AS HighestPrice \
FROM AdventureWorksLT.SalesLT.Customer C, AdventureWorksLT.SalesLT.SalesOrderHeader H, AdventureWorksLT.SalesLT.SalesOrderDetail D, AdventureWorksLT.SalesLT.Product P \
WHERE C.CustomerID = H.CustomerID AND H.SalesOrderID = D.SalesOrderID AND D.ProductID = P.ProductID AND P.Color = '" + color + \
"' GROUP BY C.CustomerID, C.FirstName, C.LastName;"

cursor.execute(myquery2)

#create output from view in desc order by last name and first name
myquery3 = "SELECT * FROM " + viewname + " ORDER BY LastName DESC, FirstName DESC;"
cursor.execute(myquery3)
result1 = cursor.fetchone()
while result1:
    out = "CustomerID: " + str(result1[0]) + " Name: " + str(result1[1]) + " " + str(result1[2]) + " \tHighestPrice: " + str(result1[3])
    print out
    result1 = cursor.fetchone()

cursor.close()
connection.commit()
connection.close()







