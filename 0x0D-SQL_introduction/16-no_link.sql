-- List all records of second_table where name is not NULL
-- Ordered by score descending
-- Usage: mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

