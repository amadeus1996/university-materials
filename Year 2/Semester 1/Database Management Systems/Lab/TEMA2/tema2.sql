-- E3
variable t_cnt_rentals number
variable t_member_name varchar2
variable t_member_id number
begin
    :t_member_name := '&nume';

    select m.member_id
    into :t_member_id
    from member m
    where lower(m.last_name) = lower(:t_member_name);

    select count(1) 
    into :t_cnt_rentals
    from rental r
    where r.member_id = :t_member_id;
        
    dbms_output.put_line(:t_cnt_rentals || ' IMPRUMUTURI');
    
    exception
        when no_data_found then
            dbms_output.put_line('INPUT GRESIT');
        when too_many_rows then
            dbms_output.put_line('MAI MULTI MEMBRI AU ACELASI NUME');
end;
/
print t_cnt_rentals


-- E4
variable t_cnt_rentals number
variable t_total_rentals number
variable t_member_name varchar2
variable t_member_id number
begin
    :t_member_name := '&nume';

    select m.member_id
    into :t_member_id
    from member m
    where lower(m.last_name) = lower(:t_member_name);

    select count(1) 
    into :t_cnt_rentals
    from rental r
    where r.member_id = :t_member_id;
    
    select count(1)
    into :t_total_rentals
    from rental;
    
    if :t_cnt_rentals > 0.75 * :t_total_rentals then
        dbms_output.put_line('Categoria 1 (a imprumutat peste 75% din titlurile existente)');
    elsif :t_cnt_rentals > 0.5 * :t_total_rentals then
        dbms_output.put_line('Categoria 2 (a imprumutat peste 50% din titlurile existente)');
    elsif :t_cnt_rentals > 0.25 * :t_total_rentals then
        dbms_output.put_line('Categoria 3 (a imprumutat peste 25% din titlurile existente)');
    else
        dbms_output.put_line('Categoria 4 (altfel)');
    end if;
    dbms_output.put_line(:t_cnt_rentals || '/' || :t_total_rentals || ' IMPRUMUTURI');
    
    exception
        when no_data_found then
            dbms_output.put_line('INPUT GRESIT');
        when too_many_rows then
            dbms_output.put_line('MAI MULTI MEMBRI AU ACELASI NUME');
end;
/
print t_cnt_rentals