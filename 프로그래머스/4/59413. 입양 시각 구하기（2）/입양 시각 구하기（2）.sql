set @h := -1;
select (@h := @h + 1) as hour, (select count(*)
                                from animal_outs
                                where hour(datetime) = @h
                                ) as count
from animal_outs
where @h < 23;
