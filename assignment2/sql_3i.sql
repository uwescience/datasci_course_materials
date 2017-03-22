.mode column

CREATE VIEW tab AS
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;


SELECT a.docid as "doc1", sum(a.count * b.count) as "S"
FROM tab a,tab b
WHERE a.term = b.term and b.docid = 'q'
GROUP BY a.docid
ORDER BY S DESC limit 10;


