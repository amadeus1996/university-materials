create or replace procedure inserare(utilizator varchar2, comanda varchar2, t_count number, error_message varchar2) as
    pragma autonomous_transaction;
begin
    insert into info_mco
    values (utilizator, sysdate, comanda, t_count, error_message);
    commit;
end;
/
create or replace function ex3
    (t_oras locations.city%type)
return number is
    t_count number;
    utilizator varchar2(20);
    error_message varchar2(50) := '';
    sql_command varchar2(1000) := 'select count(1) as "Nr. angajati" into t_count from (select 1 from job_history j join employees e on e.employee_id = j.employee_id join departments d on d.department_id = e.department_id join locations l on l.location_id = d.location_id where lower(l.city) = lower(' || t_oras || ') group by j.employee_id having count(distinct j.job_id) > 1);';
begin
    select user
    into utilizator
    from dual;
    
    select count(1) as "Nr. angajati"
    into t_count
    from (
        select 1
        from job_history j
        join employees e on e.employee_id = j.employee_id
        join departments d on d.department_id = e.department_id 
        join locations l on l.location_id = d.location_id
        where lower(l.city) = lower(t_oras)
        group by j.employee_id
        having count(distinct j.job_id) > 1);
    
    inserare(utilizator, sql_command, t_count, null);
    --if t_count = 0 then
      --  inserare(...)
    --END IF;
    return t_count;

    exception
        when others then
            inserare(utilizator, sql_command, null, sqlerrm);
end ex3;
/
select ex3('seattle') as ex3 from dual;
/
create table info_mco (
    utilizator varchar2(20),
    data date,
    comanda varchar2(1000),
    nr_linii number(4),
    eroare varchar2(50)
);
/
drop table info_mco
/
select * from info_mco