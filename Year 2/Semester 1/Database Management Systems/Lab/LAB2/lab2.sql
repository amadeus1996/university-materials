/*
EX 1
MEMBER:      (member_id)
TITLE:       (title_id)
TITLE_COPY:  (title_id, copy_id)
RENTAL:      (copy_id, member_id, book_date, title_id)
RESERVATION: (member_id, title_id, res_date)
*/


/* EX 4 */
select a.title, a.title_id, count(b.copy_id) as "Nr imprumuturi"
from title a
join rental b on a.title_id = b.title_id
where a.category = (
    select t.category
    from title t
    join rental r on r.title_id = t.title_id
    group by t.category
    order by count(r.copy_id) desc
    fetch first 1 rows only
    )
group by a.title, a.title_id;
   
   
/* EX 5 */
select t.title, t.title_id, count(r.title_id)
from title t 
join rental r on t.title_id = r.title_id
where r.act_ret_date is not null
group by t.title, t.title_id;


/* EX 6 */
select t.title, tc.copy_id, t.title_id, tc.status,
    case
        when lower(status) = 'available' and (t.title_id, tc.copy_id) in (
            select title_id, copy_id from rental where act_ret_date is null) then 'rented'
        when lower(status) = 'rented' and (t.title_id, tc.copy_id) in (
            select title_id, copy_id from rental where act_ret_date is not null) then 'available'
        else tc.status
    end as "Status corect"
from title t
join title_copy tc on t.title_id = tc.title_id;