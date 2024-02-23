select B.author_id, A.author_name, category, sum(B.price * S.sales) as total_sales
from book B, author A, book_sales S
where B.book_id = S.book_id
  and B.author_id = A.author_id
  and year(sales_date) = 2022 and month(sales_date) = 01
 group by 2, 3
 order by 1, 3 desc