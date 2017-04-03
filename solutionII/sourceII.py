# CMPT354 - A3 - Part b
# Author: Bei Bei Li - 301254625


#import the library for the database interface
import pymssql
#connect to
connection = pymssql.connect(host='cypress.csil.sfu.ca', user='s_bbli', password='3trrbAjmTjMde4P3', database='bbli354')

cursor = connection.cursor()
myquery = "EXEC dbo.AverageCost @target_color = 'Red'"
cursor.execute(myquery)

result = cursor.fetchone()[0]
print result

connection.close()



