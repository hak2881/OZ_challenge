import pymysql 
db = pymysql.connect(  ##접속 edit 하면 나오는것 입력
host='localhost', # 127.0.0.1 , 0.0.0.0 
port=3306, 
user='root', # root 이
passwd='##Dlwps753', #비밀번호 입력 
db='airbnb', #연결할 database 명 워크밴치에 있어야댐!!
charset='utf8')

cursor=db.cursor()

# 1
# SQL ="""
#     INSERT INTO Products(productID,productName,price,stockQuantity,createDate)
#     VALUES (1,'Python Book',29.99,100,'2024-12-04')
#     """
# cursor.execute(SQL)

# 2
# SQL = """
#     SELECT * FROM Customers 
#     """
# cursor.execute(SQL)

# row = cursor.fetchone()
# print(row)

# 3
# SQL = """
#     UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s
#     """
# cursor.execute(SQL,(quantity,product_id))

# 4
# sql = """
#     SELECT customerID,SUM(totalAmount) FROM Orders GROUP BY customerID
#     """
# cursor.execute(sql)
# rows = cursor.fetchall()
# for row in rows :
#     print(row)

# 5
# email = input('email 입력')
# customer = input('customerID 입력')
# sql = """
#     UPDATE Customers SET email = %s WHERE customerID = %s
#     """
# cursor.execute(sql,(email,customer))

# 6
# sql = """
#     DELETE FROM Orders WHERE orderID =%s
#     """
# cursor.execute(sql,(order_id))

# 7
# sql = """
#     SELECT * FROM Products WHERE productName = %s 
#     """
# cursor.execute(sql,(name))

# 8
# sql = """
#     SELECT * FROM Orders WHERE customerID = %s
#     """
# cursor.execute(sql,(customer_id))
# for row in cursor.fetchall():
#             print(row)

# 9 
# sql = """
#     SELECT customerID,COUNT(*) FROM Orders 
#     GROUP BY customerID 
#     ORDER BY COUNT(*) DESC
#     LIMIT 1
#     """

db.commit()

db.close()