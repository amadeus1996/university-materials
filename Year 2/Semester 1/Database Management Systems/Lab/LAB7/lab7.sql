-- E1
-- a. CURSOARE CLASICE
declare
    cursor t_job is
        select job_title
        from jobs;
        
    cursor t_angajati(t_job_title jobs.job_title%type) is
        select last_name, salary
        from employees
        where job_id = (
            select job_id 
            from jobs 
            where job_title = t_job_title);
        
    t_job_title jobs.job_title%type;
    t_last_name employees.last_name%type;
    t_salary employees.salary%type;
begin
    open t_job;
    loop
        fetch t_job into t_job_title;
        exit when t_job%notfound;
        dbms_output.put_line(t_job_title);

        open t_angajati(t_job_title);
        loop
            fetch t_angajati into t_last_name, t_salary;
            exit when t_angajati%notfound;
            dbms_output.put_line(t_last_name || ' ' || t_salary);
        end loop;
        
        close t_angajati;
        dbms_output.new_line;
    end loop;
    close t_job;
end;
/
-- b. CICLU CURSOARE
declare
    type t_info_angajat is record (
        nume    employees.last_name%type,
        salariu employees.salary%type
    );
    type t_colectie_angajati is table of t_info_angajat;
    t_job      jobs.job_title%type;
    t_angajati t_colectie_angajati;
    
    cursor t_job_cursor is 
        select job_title 
        from jobs; 
begin
    for job_record in t_job_cursor loop
        t_job := job_record.job_title;
        
        select last_name, salary
        bulk collect into t_angajati
        from employees
        where job_id = (
            select job_id from jobs where job_title = t_job);
        
        dbms_output.put_line(t_job);
        
        for i in 1..t_angajati.count loop
            dbms_output.put_line(t_angajati(i).nume || ' ' || t_angajati(i).salariu);
        end loop;
        dbms_output.new_line;
    end loop;
end;
/
-- c. CICLU CURSOARE CU SUBCERERI
declare
    type t_info_angajat is record (
        nume    employees.last_name%type,
        salariu employees.salary%type
    );
    type t_colectie_angajati is table of t_info_angajat;
    t_job      jobs.job_title%type;
    t_angajati t_colectie_angajati;
begin
    for i in (select job_title titlu from jobs) loop
        t_job := i.titlu;
        
        select last_name, salary
        bulk collect into t_angajati
        from employees
        where job_id = (
            select job_id from jobs where job_title = i.titlu);
        
        dbms_output.put_line(i.titlu);
        
        for i in 1..t_angajati.count loop
            dbms_output.put_line(t_angajati(i).nume || ' ' || t_angajati(i).salariu);
        end loop;
        dbms_output.new_line;
    end loop;
end;
/
-- d. EXPRESII CURSOR
declare
    type refcursor is ref cursor;
    cursor t_info is
        select j.job_title,
        cursor (
            select last_name as nume, salary as salariu
            from employees e
            where e.job_id = j.job_id)
        from jobs j;
        
    t_cursor refcursor;
    t_job_title jobs.job_title%type;
    t_last_name employees.last_name%type;
    t_salary employees.salary%type;
begin
    open t_info;
    loop
        fetch t_info into t_job_title, t_cursor;
        exit when t_info%notfound;
        dbms_output.put_line(t_job_title);
        
        loop
            fetch t_cursor into t_last_name, t_salary;
            exit when t_cursor%notfound;
            dbms_output.put_line(t_last_name || ' ' || t_salary);
        end loop;
        
        dbms_output.new_line;
    end loop;
    close t_info;
end;