SELECT * FROM payment LIMIT 10;

-- 1
SELECT F.title FROM film F
JOIN film_actor FA ON F.film_id=FA.film_id
JOIN actor A ON A.actor_id=FA.actor_id
WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS';
-- 2
SELECT C.name ,COUNT(*) FROM  category C
JOIN film_category F ON F.category_id = C.category_id
GROUP BY name;
-- 3
SELECT R.customer_id,last_name,rental_date,title,rental_id FROM customer C
JOIN rental R ON R.customer_id = C.customer_id
JOIN inventory I ON R.inventory_id = I.inventory_id
JOIN film F ON F.film_id = F.film_id
WHERE R.customer_id =5;
-- 4
SELECT film_id, title FROM film
ORDER BY film_id DESC LIMIT 10;

-- 조인 및 관계
-- 1
SELECT A.first_name,A.last_name
FROM actor A
JOIN film_actor FA ON A.actor_id = FA.actor_id
JOIN film F ON F.film_id = FA.film_id
WHERE F.title = 'ACADEMY DINOSAUR';
-- 2
SELECT first_name,last_name FROM customer C
JOIN rental R ON C.customer_id = R.customer_id
JOIN inventory I ON I.inventory_id = R.inventory_id
JOIN film F ON F.film_id = I.film_id
WHERE F.title = 'ACADEMY DINOSAUR';
-- 3
SELECT c.customer_id, c.first_name, c.last_name, MAX(r.rental_date) as last_rental_date, f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
GROUP BY c.customer_id, c.first_name, c.last_name, f.title;
-- 4 
SELECT f.title, AVG(DATEDIFF(r.return_date, r.rental_date)) as avg_rental_period
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title;
-- 집계 및 그룹화
-- 1
SELECT title,count(*) AS BEST_FILM_COUNT
FROM rental R
JOIN inventory I ON I.inventory_id = R.inventory_id
JOIN film F ON F.film_id = I.film_id
GROUP BY title
ORDER BY COUNT(*) DESC
LIMIT 1;
-- 2
SELECT C.name, AVG(rental_rate)
FROM category C
JOIN film_category FC ON FC.category_id = C.category_id
JOIN film F ON F.film_id = FC.film_id
GROUP BY C.name;
-- 3
SELECT YEAR(p.payment_date) as year, MONTH(p.payment_date) as month, SUM(p.amount) as total_sales
FROM payment p
GROUP BY YEAR(p.payment_date), MONTH(p.payment_date);
-- 4 
SELECT A.first_name,A.last_name, COUNT(*) AS film_count
FROM film_actor FA
JOIN film F ON F.film_id = FA.film_id
JOIN actor A ON A.actor_id = FA.actor_id
GROUP BY A.first_name,A.last_name;

-- 서브쿼리 및 고급 기능
-- 1
SELECT F.title, SUM(amount) AS best_film
FROM payment P
JOIN rental R ON R.rental_id = P.rental_id 
JOIN inventory I ON I.inventory_id = R.rental_id
JOIN film F ON F.film_id = I.film_id
GROUP BY title
ORDER BY SUM(amount) DESC
LIMIT 1;
-- 2
SELECT title,rental_rate
FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);
-- 3
SELECT first_name,last_name,COUNT(*) AS rental_count
FROM rental R 
JOIN customer C ON R.customer_id = C.customer_id
GROUP BY first_name,last_name
ORDER BY COUNT(*) DESC
LIMIT 1; 
-- 4
SELECT f.title, COUNT(r.rental_id) AS rental_count
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS'
GROUP BY f.title
ORDER BY rental_count DESC
LIMIT 1;