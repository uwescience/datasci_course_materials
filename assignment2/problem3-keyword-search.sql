select max(simi)
from (
select a.docid, b.docid, sum(a.count * b.count) simi
from v_freq a, v_freq b
where a.term = b.term
  and a.docid = 'q'
group by a.docid, b.docid
) ;

