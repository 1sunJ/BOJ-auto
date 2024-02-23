select member_name, review_text, date_format(review_date, '%Y-%m-%d') as review_date
from member_profile M, rest_review R
where M.member_id = R.member_id
  and R.member_id = (select member_id
                     from rest_review
                     group by member_id
                     order by count(*) desc
                     limit 1)
order by 3, 2