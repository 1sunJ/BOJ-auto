# 2024-12-18
select b.title, b.board_id, r.reply_id, r.writer_id, r.contents, date_format(r.created_date, "%Y-%m-%d") as created_date
from used_goods_board b
inner join used_goods_reply r
    on b.board_id = r.board_id
where year(b.created_date) = 2022
    and month(b.created_date) = 10
order by r.created_date, b.title













# select title, B.board_id, R.reply_id, R.writer_id, R.contents, date_format(R.created_date, '%Y-%m-%d') as created_date
# from used_goods_board B, used_goods_reply R
# where B.board_id = R.board_id
#   and B.created_date between '2022-10-01' and '2022-10-31'
# order by R.created_date, B.title