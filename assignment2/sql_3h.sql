.output part_h.txt
.mode column
SELECT S FROM(
SELECT a.docid as "doc1", b.docid as "doc2", sum(a.count * b.count) as "S"
FROM frequency a,frequency b
WHERE a.term = b.term
GROUP BY a.docid, b.docid)
WHERE doc1 = "10080_txt_crude" and doc2 = "17035_txt_earn";
