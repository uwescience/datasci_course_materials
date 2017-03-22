.output part_e.txt
SELECT COUNT(*) FROM(
SELECT f.docid, count(f.docid) as "D"
FROM frequency f
GROUP BY f.docid
HAVING count(f.docid) > 300
);




