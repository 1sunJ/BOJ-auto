# select book_id, author_name, date_format(published_date, '%Y-%m-%d')
# from book B, author A
# where B.author_id = A.author_id
#   and category like '경제'
# order by published_date

select book_id, author_name, date_format(published_date, '%Y-%m-%d')
from book B
join author A
  on B.author_id = A.author_id
where category like '경제'
order by published_date