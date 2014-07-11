select count(*)
from (select  docid
from frequency
where term = 'transactions' or term = 'world'
group by docid
having count(term)=2);
