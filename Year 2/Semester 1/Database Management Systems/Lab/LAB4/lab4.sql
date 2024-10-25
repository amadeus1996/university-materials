create table octombrie_mco (
    zi number(2) primary key,
    imprumuturi number(2)
);


select * 
from octombrie_mco;


declare 
    v_zi number(2);
    v_imprumuturi number(2);
begin
    for contor in 1..31 loop
        select count(1) into v_imprumuturi
        from rental 
        where extract(day from book_date) = contor;
        
        insert into octombrie_mco
        values (contor, v_imprumuturi);
    end loop;
end;