select category, sum(sales) as total_sales
from book B, book_sales S
where B.book_id = S.book_id
  and year(sales_date) = 2022 and month(sales_date) = 1
group by 1
order by 1