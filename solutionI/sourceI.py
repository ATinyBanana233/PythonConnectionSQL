# CMPT354 - A3 - Part a
# Author: Bei Bei Li - 301254625


#import the library for the database interface
import pymssql
#connect to
connection = pymssql.connect(host='cypress.csil.sfu.ca', user='s_bbli', password='3trrbAjmTjMde4P3', database='AdventureWorksLT')

cursor = connection.cursor()
myquery = 'SELECT COUNT(*) FROM SalesLT.Customer'
cursor.execute(myquery)

result = cursor.fetchone()[0]
print result

connection.close()
