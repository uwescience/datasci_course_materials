.output part_g.txt
.mode column
SELECT S FROM(
SELECT a.row_num as "R", b.col_num as "C", sum(a.value * b.value) as "S"
FROM a,b
WHERE a.col_num = b.row_num
GROUP BY a.row_num, b.col_num)
WHERE R = 2 and C = 3;

