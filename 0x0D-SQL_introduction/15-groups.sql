-- List the number of records with the same score in the table second_table
-- The list should be sorted by the number of records descending
-- Usage: mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;

