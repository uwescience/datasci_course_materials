select simi
from (
select a.docid as a_doc_id, b.docid as b_doc_id, sum(a.count * b.count) as simi
from frequency a, frequency b
where a.term = b.term
  and a.docid < b.docid
  and a_doc_id = '10080_txt_crude'
  and b_doc_id = '17035_txt_earn'
group by a.docid, b.docid
);
