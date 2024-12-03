-- 1 . 초급
-- CREATE
-- (1)
DESC customers;
SELECT * FROM customers LIMIT 1;
INSERT INTO customers(customerNumber,customerName,contactLastName,contactFirstName,
					phone,addressLine1,city,postalCode,country,
                    salesRepEmployeeNumber,creditLimit)
VALUES (500,'KIMHAK','KIM',
		'HAK','0000-0000','pohang','daegu','444','Seoul',1370,13.3),
        (501,'KIMHAKd','KIM',
		'HAK','0000-0000','pohang','daegu','444','Seoul',1370,13.3);
-- (2)
SELECT * FROM products LIMIT 1;
INSERT INTO products(productCode,productName,productLine,productScale,
					productVendor,productDescription,quantityInStock,
                    buyPrice,MSRP)
VALUES ('S10_1999','choper','Motorcycles','1:4',
		' HAK','i dont know', 130,30.33,10.2);
-- (3)
SELECT * FROM employees LIMIT 1;
INSERT INTO employees(employeeNumber,lastName,firstName,extension,
					email,officeCode,jobTitle)
VALUES (2000,'hak','kim','x4000','gkr054@asdf.com','1','king');
-- (4)
SELECT * FROM offices LIMIT 1;
INSERT INTO offices(officeCode,city,phone,addressLine1,addressLine2,state,
					country,postalCode,territory)
VAlUES (20,'pohang','123-456','dong','tan','ca','seoul','12345','na');
-- (4) 중급
SELECT * FROM orders ORDER BY orderNumber DESC LIMIT 1;
SELECT * FROM orderdetails ORDER BY orderNumber DESC LIMIT 1;
INSERT INTO orders(orderNumber,orderDate,requiredDate,status,customerNumber)
VALUES (10427,'2000-01-01','2999-09-01','por','119');
INSERT INTO orderdetails(orderNumber,productCode ,quantityOrdered ,priceEach ,orderLineNumber)
VALUES (10427,'S50_1392',18,94.22,2);
-- (5)
SELECT * FROM orders ORDER BY orderNumber DESC LIMIT 1;
INSERT INTO orders(orderNumber,orderDate, requiredDate ,status, customerNumber)
VALUES (10426,'2000-01-01','2999-01-01','process',119);
-- (6)
SELECT * FROM orderdetails ORDER BY orderNumber DESC LIMIT 1;
INSERT INTO orders(orderNumber,orderDate, requiredDate ,status, customerNumber)
VALUES (10429,'2000-01-01','2999-01-01','process',119);
INSERT INTO orderdetails(orderNumber,productCode ,quantityOrdered ,priceEach ,orderLineNumber)
VALUES (10429,'S10_1999',18,94.22,2);
-- (7)
SELECT * FROM payments ORDER BY customerNumber DESC LIMIT 1;
INSERT INTO payments(customerNumber,checkNumber, paymentDate, amount)
VALUES(500,'MN889999','2999-01-01',10.43);
-- (8)
SELECT * FROM productlines ORDER BY productLine DESC LIMIT 1;
INSERT INTO productlines(productLine ,textDescription)
VALUES ('car','good car');
-- (9)
SELECT * FROM customers ORDER BY customerNumber DESC LIMIT 1;
INSERT INTO customers(customerNumber,customerName,contactLastName,contactFirstName,
					phone,addressLine1,city,postalCode,country,
                    salesRepEmployeeNumber,creditLimit)
VALUES (502,'KIMHA3K','KIM',
		'HAK','0000-0000','seoul','daegu','444','korea',1370,13.3);
-- (10)
SELECT * FROM products ORDER BY productCode DESC LIMIT 1;
INSERT INTO products(productCode,productName,productLine,productScale,
					productVendor,productDescription,quantityInStock,
                    buyPrice,MSRP)
VALUES ('S10_19993','choper','Ships','1:4',
		' HAK','i dont know', 130,30.33,10.2);

-- 2. 읽기
-- (1)~(10)
SELECT * FROM customers;
SELECT productName FROM products;
SELECT firstName,jobTitle FROM employees;
SELECT territory FROM offices;
SELECT * FROM orders ORDER BY orderNumber DESC LIMIT 10;
SELECT * FROM orderdetails WHERE orderNumber = 10425 and productCode='S10_4962';
SELECT * FROM payments WHERE customerNumber = 500;
SELECT productLine,textDescription FROM productlines;
SELECT * FROM customers WHERE city='San Rafael';
SELECT * FROM products WHERE 50<buyPrice<70;

-- 3. 갱신
-- (1)~(10)
SELECT quantityInStock,buyPrice FROM products;
UPDATE customers SET addressLine1 = 'new address' WHERE addressLine1 ='Vinbæltet 34';
UPDATE products SET buyPrice = 3.3 WHERE buyPrice = 48.81;
UPDATE employees SET jobTitle = 'King' WHERE firstName ='Mary';
UPDATE offices SET phone = '332.445.67' WHERE officeCode='1';
UPDATE orders SET status = 'car' WHERE orderNumber = '10100';
UPDATE orderdetails SET quantityOrdered = 1 WHERE productCode='S18_2248';
UPDATE payments SET amount = 999999.99 WHERE checkNumber = 'OM314933';
UPDATE productlines SET textDescription = 'is good' WHERE productLine='Planes';
UPDATE customers SET postalCOde = '11' WHERE customerNumber = 103;
UPDATE products SET buyPrice = 10 WHERE quantityInStock <5000 ;

-- 4. 삭제
-- (1)~(10)
DELETE FROM payments WHERE customerNumber =500; 
DELETE FROM customers WHERE customerNumber =500; 

DELETE FROM orderdetails WHERE productCode = 'S10_1999';
DELETE FROM products WHERE productCode = 'S10_1999';

DELETE FROM employees WHERE employeeNumber = 2000;

DELETE FROM offices WHERE officeCode = 20;

DELETE FROM orderdetails WHERE orderNumber = 10427;
DELETE FROM orders WHERE orderNumber = 10427;

DELETE FROM orders WHERE orderNumber = 10426;
DELETE FROM orderdetails WHERE orderNumber = 10426;

DELETE FROM customers WHERE customerNumber =497; 
DELETE FROM payments WHERE customerNumber =497; 

DELETE FROM payments WHERE customerNumber = 1;
DELETE FROM customers WHERE customerID = 1;

DELETE FROM productlines WHERE productLine ='car';

DELETE FROM payments WHERE customerNumber =500; 
DELETE FROM customers WHERE customerNumber =500; 

DELETE FROM orderdetails WHERE productCode = 'S10_1999';
DELETE FROM products WHERE productCode = 'S10_1999';



