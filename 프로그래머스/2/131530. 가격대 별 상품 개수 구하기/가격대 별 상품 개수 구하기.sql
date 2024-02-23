select truncate(price, -4) as price_group, count(*) as products
from product
group by 1
order by 1