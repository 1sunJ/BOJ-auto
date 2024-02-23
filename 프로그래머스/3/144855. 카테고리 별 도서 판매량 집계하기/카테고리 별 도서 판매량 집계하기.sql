select category, sum(sales) as total_sales
from book B, book_sales S
where B.book_id = S.book_id
  and date_format(sales_date, '%Y-%m-%d') like '2022-01%'
group by 1
order by 1