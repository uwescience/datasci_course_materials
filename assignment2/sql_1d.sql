.output part_d.txt
SELECT COUNT(*) FROM(
SELECT DISTINCT f.docid, count(f.docid)
FROM frequency f
WHERE f.term = "law" or f.term = "legal"
GROUP BY f.docid
);
