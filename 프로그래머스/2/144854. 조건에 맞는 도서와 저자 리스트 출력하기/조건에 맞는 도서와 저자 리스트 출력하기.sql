select book_id, author_name, date_format(published_date, '%Y-%m-%d')
from book B, author A
where B.author_id = A.author_id
  and category like '경제'
order by published_date

