select I.animal_id, I.name
from animal_ins I, animal_outs O
where I.animal_id = O.animal_id
  and I.datetime > O.datetime
order by I.datetime