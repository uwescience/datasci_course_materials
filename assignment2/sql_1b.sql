.output part_b.txt
SELECT count(*) FROM (
SELECT f.term
FROM frequency f
WHERE f.docid = "10398_txt_earn" and f.count = 1
);