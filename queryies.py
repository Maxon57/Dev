create_table_employees = """CREATE TABLE IF NOT EXISTS employees (
id INT PRIMARY KEY NOT NULL,
parentId INTEGER,
name VARCHAR NOT NULL,
type INTEGER NOT NULL,
FOREIGN KEY (parentId) REFERENCES employees(id)
);
"""

get_employees = f"""
CREATE OR REPLACE FUNCTION get_employee(employee_id int)
    RETURNS TABLE(id int, parentid int, name varchar, type int) AS $$
DECLARE
    city_id numeric;
begin
  WITH RECURSIVE city_search AS (
    SELECT employees.id, employees.parentId, employees.type
    FROM employees
    WHERE employees.id = employee_id and employees.type = 3

    UNION

    SELECT e.id, e.parentId, e.type
    FROM employees e
    JOIN city_search cs ON e.id = cs.parentId
  )
  SELECT city_search.id
  INTO city_id
  FROM city_search
  WHERE city_search.type = 1;

  RETURN query
  WITH RECURSIVE employee_search AS (
    SELECT employees.id, employees.parentId, employees.name, employees.type
    FROM employees
    WHERE employees.id = city_id

    UNION

    SELECT e.id, e.parentId, e.name, e.type
    FROM employees e
      JOIN employee_search es ON es.id = e.parentId
  )
  SELECT *
  FROM employee_search
  where employee_search.type != 2
  order by id asc;
end; $$ LANGUAGE plpgsql;

select parentid, name FROM get_employee(%s);
"""
