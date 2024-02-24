select user_id, nickname, sum(price) as total_sales
from used_goods_board B, used_goods_user U
where B.writer_id = U.user_id
  and status like 'done'
group by U.user_id
having sum(price) >= 700000
order by 3