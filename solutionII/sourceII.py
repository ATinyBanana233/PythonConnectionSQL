# CMPT354 - A3 - Part b
# Author: Bei Bei Li - 301254625


#import the library for the database interface
import pymssql
#connect to
connection = pymssql.connect(host='', user='', password='', database='')

cursor = connection.cursor()
myquery = "EXEC dbo.AverageCost @target_color = 'Red'"
cursor.execute(myquery)

result = cursor.fetchone()[0]
print result

connection.close()



