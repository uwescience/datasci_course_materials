.output part_a.txt
SELECT count(*) FROM (
  SELECT *
  FROM frequency f
  WHERE f.docid = "10398_txt_earn"
);
