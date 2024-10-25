/* LAB 2 - EX 9 */
select t.title, m.first_name, m.last_name, count(r.copy_id) as "Nr imprumutari"
from title t 
left join rental r on r.title_id = t.title_id
left join member m on m.member_id = r.member_id
group by t.title, m.first_name, m.last_name;


/* LAB 2 - EX 11 */
select max(s.nr), t.title, tc.status from (
    select r.title_id, r.copy_id, count(*) as nr from rental r
    group by r.title_id, r.copy_id) s
left join title_copy tc on s.copy_id = tc.copy_id and s.title_id = tc.title_id
left join title t on t.title_id = s.title_id
group by t.title, tc.status;


/* LAB 3 - EX 6 */
VARIABLE rezultat VARCHAR2(35)
variable angajati number(2)
BEGIN
 SELECT department_name, count(*)
 INTO :rezultat, :angajati
 FROM employees e, departments d
 WHERE e.department_id=d.department_id
 GROUP BY department_name
 HAVING COUNT(*) = (SELECT MAX(COUNT(*))
 FROM employees
GROUP BY department_id);
 DBMS_OUTPUT.PUT_LINE('Departamentul '|| :rezultat || ', ' || :angajati);
END;
/
PRINT rezultat
print angajati