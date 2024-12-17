select ri.rest_id, rest_name, food_type, favorites, address, round(avg(rr.review_score), 2) as SCORE
from rest_info ri
inner join rest_review rr
    on ri.rest_id = rr.rest_id
where ri.address like "서울%"
group by rest_id
order by score desc, favorites desc


# select *
# from rest_info
# where address like "서울%"

# select *
# from rest_review
# where rest_id in (00001, 00002, 00003, 00004, 00005, 00008)
# order by rest_id