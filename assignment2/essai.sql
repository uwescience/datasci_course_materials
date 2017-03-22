.mode column
SELECT COUNT(*) FROM(
SELECT f.docid, sum(f.count)
FROM Frequency f
GROUP BY f.docid
HAVING sum(f.count)>300)
;

