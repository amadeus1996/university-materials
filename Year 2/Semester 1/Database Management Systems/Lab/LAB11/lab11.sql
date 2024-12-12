-- 5: a), b), c), d), e)
create table info_dept_mco as (
    select d.department_id as id, d.department_name nume_dept, sum(e.salary) as plati
    from departments d 
    join employees e on e.department_id = d.department_id
    group by d.department_id, d.department_name);
	
create table info_emp_mco as (
    select e.employee_id as id, e.last_name as nume, e.first_name as prenume, 
    e.salary as salariu, d.id as id_dept
    from employees e
    join info_dept_mco d on e.department_id = d.id);
	
create or replace view v_info_mco as
    select e.id, e.nume, e.prenume, e.salariu, e.id_dept, d.nume_dept, d.plati
    from info_emp_mco e 
    join info_dept_mco d on d.id = e.id_dept;
	
select *
from user_updatable_columns
where table_name = 'V_INFO_MCO';

/
create or replace trigger trig5_mco
instead of insert or delete or update on v_info_mco
for each row
begin
    if inserting then
     -- inserarea in vizualizare determina inserarea
    -- in info_emp_*** si reactualizarea in info_dept_***
    -- se presupune ca departamentul exista
    INSERT INTO info_emp_mco
    VALUES (:NEW.id, :NEW.nume, :NEW.prenume, :NEW.salariu, :NEW.id_dept);
    UPDATE info_dept_mco
    SET plati = plati + :NEW.salariu
    WHERE id = :NEW.id_dept;
    
    ELSIF DELETING THEN
    -- stergerea unui salariat din vizualizare determina
    -- stergerea din info_emp_*** si reactualizarea in
    -- info_dept_***
    DELETE FROM info_emp_mco
    WHERE id = :OLD.id;
    UPDATE info_dept_mco
    SET plati = plati - :OLD.salariu
    WHERE id = :OLD.id_dept;
    
    ELSIF UPDATING ('salariu') THEN
 /* modificarea unui salariu din vizualizare determina
 modificarea salariului in info_emp_*** si reactualizarea
 in info_dept_*** */
    UPDATE info_emp_mco
    SET salariu = :NEW.salariu
    WHERE id = :OLD.id;
    UPDATE info_dept_mco
    SET plati = plati - :OLD.salariu + :NEW.salariu
    WHERE id = :OLD.id_dept;
    
    ELSIF UPDATING ('id_dept') THEN
 /* modificarea unui cod de departament din vizualizare
 determina modificarea codului in info_emp_***
 si reactualizarea in info_dept_*** */
    UPDATE info_emp_mco
    SET id_dept = :NEW.id_dept
    WHERE id = :OLD.id;
    UPDATE info_dept_mco
    SET plati = plati - :OLD.salariu
    WHERE id = :OLD.id_dept;
    UPDATE info_dept_mco
    SET plati = plati + :NEW.salariu
    WHERE id = :NEW.id_dept;
    END IF;
END;
/


-- E3
create table info_dept_mco as (
    select d.department_id as id, d.department_name nume_dept, 
    sum(e.salary) as plati, count(1) as numar
    from departments d 
    join employees e on e.department_id = d.department_id
    group by d.department_id, d.department_name);
	
create or replace trigger trig_E3
after delete or insert on info_emp_mco
for each row
begin
    if inserting then
        update info_dept_mco
        set numar = numar + 1
        where id = :new.id_dept;
    elsif deleting then
        update info_dept_mco
        set numar = numar - 1
        where id = :old.id_dept;
    end if;
end;
/