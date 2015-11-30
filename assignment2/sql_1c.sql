.output part_c.txt
SELECT count(*) FROM(
SELECT f.term
FROM frequency f
WHERE f.docid = "10398_txt_earn" and f.count = 1
UNION
SELECT f.term
FROM frequency f
WHERE f.docid = "925_txt_trade" and f.count = 1
);