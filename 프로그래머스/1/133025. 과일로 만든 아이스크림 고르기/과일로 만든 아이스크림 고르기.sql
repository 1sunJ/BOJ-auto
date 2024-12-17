select fh.flavor
from first_half fh, icecream_info ii
where total_order > 3000
    and fh.flavor = ii.flavor and ii.ingredient_type = "fruit_based"
order by total_order desc



/*
select fh.flavor
from first_half fh, icecream_info ii
where total_order > 3000 and ingredient_type = 'fruit_based' and fh.flavor = ii.flavor
order by total_order desc
*/
