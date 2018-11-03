import mysql.connector
import sys

db= mysql.connector.connect(user="root",password="asdfghjkl;",host="localhost",database="dsaa")

mycursor = db.cursor()

path="/home/san/aaa/dssa-4.jpg"

#sql= "CREATE TABLE  test (address varchar(255) primary key, id INT(10) AUTO_INCREMENT"
#mycursor.execute("CREATE TABLE  test (address varchar(255) , id INT AUTO_INCREMENT primary key, UNIQUE(address) )")
sql = 'INSERT INTO test (address , name) VALUES (%s ,%s)'
val = [("/home/san/aaa/OS-1.jpg", "jpg"),
	  ("/home/san/aaa/OS-2.jpg", "jpg"),
	  ("/home/san/aaa/example_03.png", "png")
 	  ]
mycursor.executemany(sql, val)
db.commit()
# print """ 
# +=========================================+
# |    Please select  page no. of Book	  |
# +=========================================+
# 	  """
# mycursor.execute("select address,id from test")

# data = mycursor.fetchall()
# #print "san----",data
# a=[]
# for i in data:
# 	a.append(i[0])
# 	#print i

# for i in range(len(a)):
# 	print i,".",a[i]
mycursor.close()
db.close()
sys.exit()

