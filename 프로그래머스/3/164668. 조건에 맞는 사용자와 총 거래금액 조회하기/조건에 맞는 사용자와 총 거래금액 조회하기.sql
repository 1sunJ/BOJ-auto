# select user_id
# from used_goods_board B, used_goods_user U
# group by B.writer_id
# where B.sum(select price
#             from used_goods_board B2
#             where B1.writer_id = B2.writer_id)
#             >= 700000

select B.writer_id, U.nickname, sum(price) as total_sales
from used_goods_board B, used_goods_user U
where status = 'Done'
  and B.writer_id = U.user_id
group by B.writer_id
having total_sales >= 700000
order by total_sales

# SELECT USER_ID, NICKNAME, sum(PRICE)TOTAL_SALES
# FROM USED_GOODS_BOARD as b, USED_GOODS_USER as u
# WHERE b.WRITER_ID = u.USER_ID
# and STATUS = 'DONE'
# group by 1
# having TOTAL_SALES >= 700000
# order by 3