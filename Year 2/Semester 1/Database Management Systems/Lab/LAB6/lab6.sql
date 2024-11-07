create or replace type tip_orase_aux is table of varchar2(20);
/
create table excursie_aux (
    cod_excursie number(4) primary key,
    denumire varchar2(20),
    status varchar2(10)
);
/
alter table excursie_aux
add (orase tip_orase_aux)
nested table orase store as tabel_orase_aux;
/
select * from excursie_aux;
/
declare
    t_cod_excursie excursie_aux.cod_excursie%type;
    t_oras_aux     varchar2(20);
    t_oras_aux_2   varchar2(20);
    t_orase        tip_orase_aux;
begin
    -- a)
--    insert into excursie_aux
--    values (1, 'Excursie 1', 'Disponibil', tip_orase_aux('Viena', 'Barcelona', 'Berlin'));
--    insert into excursie_aux
--    values (2, 'Excursie 2', 'Disponibil', tip_orase_aux('Tokyo', 'Istanbul'));
--    insert into excursie_aux
--    values (3, 'Excursie 3', 'Anulat',     tip_orase_aux('Roma'));
--    insert into excursie_aux
--    values (4, 'Excursie 4', 'Disponibil', tip_orase_aux('Londra', 'Amsterdam', 'Paris', 'Lisabona'));
--    insert into excursie_aux
--    values (5, 'Excursie 5', 'Anulat',     tip_orase_aux('Bucuresti', 'Brasov'));
    
    -- punctul b) - part 1
--    t_cod_excursie := &cod;
--    t_oras_aux    := '&oras';
--    dbms_output.put(t_cod_excursie || ' ' || t_oras_aux);
--    dbms_output.new_line;
--
--    select orase 
--    into t_orase 
--    from excursie_aux 
--    where cod_excursie = t_cod_excursie;
--    
--    t_orase.extend;
--    t_orase(t_orase.count) := t_oras_aux;
--
--    update excursie_aux
--    set orase = t_orase
--    where cod_excursie = t_cod_excursie;
--    
--    for i in t_orase.first..t_orase.last loop
--        dbms_output.put(t_orase(i) || ' ');
--    end loop;
--    dbms_output.new_line;

    -- punctul b) - part 2
    t_cod_excursie := &cod;
    t_oras_aux    := '&oras';
    dbms_output.put(t_cod_excursie || ' ' || t_oras_aux);
    dbms_output.new_line;

    select orase 
    into t_orase 
    from excursie_aux 
    where cod_excursie = t_cod_excursie;
    
    t_orase.extend;
    for i in reverse 3..t_orase.last loop
        t_orase(i) := t_orase(i - 1);
    end loop;
    
    t_orase(2) := t_oras_aux;
    
    update excursie_aux
    set orase = t_orase
    where cod_excursie = t_cod_excursie;
    
    for i in t_orase.first..t_orase.last loop
        dbms_output.put(t_orase(i) || ' ');
    end loop;
    dbms_output.new_line;
    
    -- punctul b) - part 3
--    t_oras_aux   := '&oras';
--    t_oras_aux_2 := '&oras';
    
    
end;
/
rollback;
/
commit;
/
delete from excursie_aux;
/