with recursive times as (
    select 0 as time
    union all
    select time + 1 as num
    from times
    where time < 23
)

select time as hour, count(animal_id) as count
from times
    left outer join animal_outs
        on time = hour(datetime)
group by hour
order by time