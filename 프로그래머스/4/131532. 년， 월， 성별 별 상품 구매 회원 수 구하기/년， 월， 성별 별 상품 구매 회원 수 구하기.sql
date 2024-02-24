select year(sales_date), month(sales_date), gender, count(distinct S.user_id) as users
from user_info U, online_sale S
where U.user_id = S.user_id
  and gender is not null
group by 1, 2, 3
order by 1, 2, 3