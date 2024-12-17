# 2024-12-18
select name
from animal_ins
where datetime = (select datetime
                 from animal_ins
                 order by datetime
                 limit 1)














# select name
# from animal_ins
# order by datetime
# limit 1