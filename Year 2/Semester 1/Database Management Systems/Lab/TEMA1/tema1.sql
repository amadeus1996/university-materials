/*
PUNCTUL a)
PIESA: O piesa are un titlu, o durata (specificata in secunde) si un identificator unic "id_piesa". 
CONCERT: Un concert va avea loc la o data fixata. Concertele au un identificator unic "id_concert".
REPERTORIU: Toate piesele care vor fi interpretate la fiecare concert; cheia primara compusa este formata din "id_piesa" si "id_concert".
PIESA_e_interpretata_la_CONCERT: relatie de tip many-to-many intre entitatile PIESA si CONCERT, ilustrand conexiunea dintre acestea. Cardinalitatea minima este 1:0 (la un
concert trebuie interpretata macar o piesa, iar o piesa poate sa nu fie interpretata deloc), cea maxima fiind M:M (la un concert pot fi interpretate mai multe piese, iar o piesa poate fi interpretata la mai multe concerte). Denumirea acestei relatii in diagrama conceptuala va fi "REPERTORIU".



PUNCTUL b)
POZA ATASATA


PUNCTUL c)
Relatia este de tip many-to-many; tabela asociativa "REPERTORIU" rezolva aceasta problema. 
Noua tabela va avea o cheie primara compusa formata din cheile externe "id_piesa" si "id_concert"; cheile externe fac referinta la "id_piesa" din tabela PIESA si "id_concert" din tabela CONCERT. Nu mai exista alte atribute pentru tabela REPERTORIU.


PUNCTUL d)
POZA ATASATA
*/


/* PUNCTUL e) */
CREATE TABLE PIESA (
    id_piesa NUMBER(4) PRIMARY KEY,
    titlu VARCHAR(30) NOT NULL,
    durata NUMBER(4) NOT NULL
);


CREATE TABLE CONCERT (
    id_concert NUMBER(4) PRIMARY KEY,
    data DATE NOT NULL
);


CREATE TABLE REPERTORIU (
    id_piesa NUMBER(4) NOT NULL,
    id_concert NUMBER(4) NOT NULL,
    PRIMARY KEY (id_piesa, id_concert),
    FOREIGN KEY (id_piesa) REFERENCES PIESA(id_piesa),
    FOREIGN KEY (id_concert) REFERENCES CONCERT(id_concert)
);


/* PUNCTUL f) */
INSERT INTO PIESA
VALUES(1, 'Road Trippin', 205);
INSERT INTO PIESA
VALUES(2, 'Scar Tissue', 216);
INSERT INTO PIESA
VALUES(3, 'Tear', 317);
INSERT INTO PIESA
VALUES(4, 'By the Way', 338);
INSERT INTO PIESA
VALUES(5, 'Snow (Hey Oh)', 335);
INSERT INTO PIESA
VALUES(6, 'Dani California', 283);
COMMIT;


INSERT INTO CONCERT
VALUES(100, '05-AUG-2024');
INSERT INTO CONCERT
VALUES(110, '28-DEC-2024');
INSERT INTO CONCERT
VALUES(120, '12-OCT-2024');
INSERT INTO CONCERT
VALUES(130, '02-NOV-2024');
INSERT INTO CONCERT
VALUES(140, '14-FEB-2025');
COMMIT;


INSERT INTO REPERTORIU
VALUES(1, 100);
INSERT INTO REPERTORIU
VALUES(2, 100);
INSERT INTO REPERTORIU
VALUES(3, 110);
INSERT INTO REPERTORIU
VALUES(4, 110);
INSERT INTO REPERTORIU
VALUES(3, 120);
INSERT INTO REPERTORIU
VALUES(6, 120);
INSERT INTO REPERTORIU
VALUES(2, 130);
INSERT INTO REPERTORIU
VALUES(1, 130);
INSERT INTO REPERTORIU
VALUES(5, 140);
INSERT INTO REPERTORIU
VALUES(6, 140);
COMMIT;


/* 
CERINTA SQL: Sa se afiseze titlul si durata pentru fiecare piesa care va fi interpretata de exact 2 ori in total la concertele care vor avea loc in anul 2024. Se va folosi o subcerere corelata, iar rezultatul va fi ordonat descrescator dupa durata.
*/ 

select p.titlu, p.durata
from piesa p
where exists (
    select 1
    from piesa a
    join repertoriu r on a.id_piesa = r.id_piesa
    join concert c on r.id_concert = c.id_concert
    where p.id_piesa = a.id_piesa
    and extract(year from c.data) = 2024
    having count(1) = 2
)
order by p.durata desc;