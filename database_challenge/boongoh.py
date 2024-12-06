import pymysql 
db = pymysql.connect(  ##접속 edit 하면 나오는것 입력
host='localhost', # 127.0.0.1 , 0.0.0.0 
port=3306, 
user='root', # root 이
passwd='0000', #비밀번호 입력 
db='db_test', #연결할 database 명 워크밴치에 있어야댐!!
charset='utf8')

try : 
    with db.cursor() as cursor :

        # 1번
        # sql = """
        #     INSERT INTO users(first_name,last_name,email,password,address,gender,is_active,is_staff)
        #     VALUES ('8ki','joa','8ki@.com','8888','8kicity','MALE',1,1)
        #     """

        # 2번
        # sql = """
        #     UPDATE users SET address = 'joa@a.com' 
        #     WHERE first_name='8ki' and last_name='joa'
        #     """

        # 3번
        # sql1="""
        #     INSERT INTO sales_records(user_id,store_id,is_refund,created_at)
        #     VALUES (11,1,0,NOW());
        #     """

        # sql2="""
        #     INSERT INTO sales_items(sales_record_id,product_id,quantity,created_at)
        #     VALUES (LAST_INSERT_ID(),11,3,NOW());
        #     """
        # cursor.execute(sql1)
        # cursor.execute(sql2)
        # sql1 = """
        #     INSERT INTO sales_records(user_id,store_id,is_refund,created_at)
        #     VALUES (11,1,0,NOW());
        #     """
        # cursor.execute(sql1)
        # sql2="""
        #     INSERT INTO sales_items(sales_record_id,product_id,quantity,created_at)
        #     VALUES (LAST_INSERT_ID(),12,2,NOW());
        #     """
        # cursor.execute(sql2)
        # sql1="""
        #     INSERT INTO sales_records(user_id,store_id,is_refund,created_at)
        #     VALUES (11,1,0,NOW());
        #     """
        # sql2="""
        #     INSERT INTO sales_items(sales_record_id,product_id,quantity,created_at)
        #     VALUES (LAST_INSERT_ID(),13,5,NOW());
        #     """

        # 4번
        # sql1 ="""
        #     INSERT INTO suppliers(name,address,contact,is_active)
        #     VALUES ('hak','dong','dd',1);
        #     """
        # sql2 = """
        #     INSERT INTO order_records(employee_id,supplier_id,change_date,raw_material_id,quantity,create_at)
        #     VALUES (3,LAST_INSERT_ID(),NOW(),2,10,NOW()),
        # 	(4,LAST_INSERT_ID(),NOW(),1,20,NOW()),
        #     (5,LAST_INSERT_ID(),NOW(),4,30,NOW())
        #     """

        # 5번
        # sql1 = """
        #     INSERT INTO stocks(raw_material_id,pre_quantity,quantity,change_type,store_id,create_at)
        #     VALUES (3,40,100,'IN',3,NOW()),
        # 	(5,30,20,'OUT',1,NOW()),
        # 	(1,10,700,'IN',2,NOW())
        #     """
        # cursor.execute(sql1)
        # sql2 = """
        #     SELECT * FROM stocks
        #     ORDER BY create_at DESC
        #     LIMIT 3
        #     """
        # cursor.execute(sql2)
        # cursor.execute(sql2)
        # rows = cursor.fetchall()
        # for row in rows :
        #     print(row)
        # db.commit()
        # 6번
        sql = """
            SELECT P.name,SI.quantity,P.price,quantity*price AS total_price FROM users U 
            JOIN sales_records SR ON SR.user_id = U.id
            JOIN sales_items SI ON SI.sales_record_id = SR.id
            JOIN products P ON P.id = SI.product_id
            WHERE U.first_name = '8ki' AND U.last_name = 'joa'
            ORDER BY P.price DESC;
            """
        cursor.execute(sql)
        rows=cursor.fetchall()
        for row in rows :
            print(row)
    db.commit()
finally : 
    db.close()
