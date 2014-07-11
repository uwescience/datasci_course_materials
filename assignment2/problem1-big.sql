select count(*)
from (
select docid, sum(count)
from frequency
group by docid
having sum(count)>300
);
