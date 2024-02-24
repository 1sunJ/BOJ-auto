# select car_id,
#        case
#         when '2022-10-16' between date_format(start_date, '%Y-%m%-d') and date_format(end_date, '%Y-%m%-d')
#             then '대여 중'
#         else '대여 가능'
#         end as availability
# from car_rental_company_rental_history
# group by 1
# order by 1 desc

select car_id,
        case
            when car_id in (select car_id
                            from car_rental_company_rental_history
                            where '2022-10-16' between start_date and end_date)
                then '대여중'
            else '대여 가능'
        end as availability
from car_rental_company_rental_history
group by 1
order by 1 desc









# select car_id,
#     case
#         when car_id in (select car_id
#                         from car_rental_company_rental_history
#                         where '2022-10-16' between start_date and end_date) then '대여중'
#         else '대여 가능'
#     end as 'availability'
# from car_rental_company_rental_history
# group by car_id
# order by car_id desc

# SELECT CAR_ID,
#     max(CASE WHEN '2022-10-16' 
#         BETWEEN START_DATE AND END_DATE
#         THEN "대여중"
#         ELSE "대여가능" END) AS    AVAILABILITY
#     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# GROUP BY CAR_ID
# ORDER BY CAR_ID DESC;

# select *
# from car_rental_company_rental_history
# order by car_id desc

# select *
# from car_rental_company_rental_history
# group by car_id
# order by car_id desc;