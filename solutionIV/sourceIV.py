# CMPT354 - A3 - Part B - Part IV
# Author: Bei Bei Li - 301254625

#import the library for the application
import os
import pymssql

        
#creating a new file for outputIVa.html
def write_file(path, data): 
    f = open(path, 'w')
    f.write(data)
    f.close()


#connect to database
connection = pymssql.connect(host='', user='', password='', database='')

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
if ((color == "Silver/Black") or (color == "silver/black") or  (color == "Silver/black") or (color == "silver/Black")):
    viewname = 'SilverBlackSpending'
else:
    viewname = color + 'Spending'
price = input("please provide a price for the chosen color: ")
print

#getting the avg_price for the color
myquery1 = "EXEC dbo.AverageCost @target_color = '" + color + "'"
cursor.execute(myquery1)
avg_price = cursor.fetchone()[0]

#comparing the given price and the avg_price

#lower given price than avg_price will return msg
if price < avg_price:
    print "Price is too low for " + color + "."
#else do the write required HTML sorted by descending order highest price
else:
    check = "IF OBJECT_ID('dbo." + viewname + "','v') IS NOT NULL DROP VIEW dbo." + viewname + ";"
    cursor.execute(check)
    myquery2 = "CREATE VIEW " + viewname + " AS SELECT C.CustomerID, C.FirstName, C.LastName, MAX(D.UnitPrice) AS HighestPrice \
    FROM AdventureWorksLT.SalesLT.Customer C, AdventureWorksLT.SalesLT.SalesOrderHeader H, AdventureWorksLT.SalesLT.SalesOrderDetail D, AdventureWorksLT.SalesLT.Product P \
    WHERE C.CustomerID = H.CustomerID AND H.SalesOrderID = D.SalesOrderID AND D.ProductID = P.ProductID AND P.Color = '" + color + \
    "' GROUP BY C.CustomerID, C.FirstName, C.LastName;"
    cursor.execute(myquery2) 
    myquery3 = "SELECT * FROM " + viewname + " ORDER BY HighestPrice DESC, LastName DESC, FirstName DESC;"
    cursor.execute(myquery3)
    html = "<!DOCTYPE html><html lang=\"en-US\"><head><title>OutputIVa</title></head><body><div><h2>"
    html = html + color + "</h2><table><tr><th>CustomerID</th><th>FirstName</th><th>LastName</th><th>HighestPrice</th></tr>"
    row = cursor.fetchone()
    while row:
        html = html + "<tr><td>" + str(row[0]) + "</td><td>" + row[1] + "</td><td>" + row[2] + "</td><td>" + str(row[3]) + "</td></tr>"
        row = cursor.fetchone()
    html = html + "</table></div></body></html>"
    write_file('outputIVa.html', html)
    print "Output completed. Please check local directory for the created html file."

cursor.close()
connection.commit()
connection.close()
