# set @h := -1;
# select (@h := @h + 1) as hour, (select count(*)
#                                 from animal_outs
#                                 where hour(datetime) = @h
#                                 ) as count
# from animal_outs
# where @h < 23;

with recursive times as (
    select 0 as time
    union all
    select time + 1 as num
    from times
    where time < 23
)

select time as hour, count(animal_id) as count
from times
    left join animal_outs
        on time = hour(datetime)
group by 1
order by time

