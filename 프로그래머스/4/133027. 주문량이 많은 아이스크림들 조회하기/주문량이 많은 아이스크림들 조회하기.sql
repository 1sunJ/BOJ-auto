select J.flavor
from first_half H, july J
where H.flavor = J.flavor
group by J.flavor
order by sum(H.total_order) + sum(J.total_order) desc
limit 3