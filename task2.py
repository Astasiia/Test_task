import psycopg2

if __name__ == '__main__':
    connection = psycopg2.connect(user="USER", password="PASSWORD", host="localhost", port="1111", database="DB")
    cursor = connection.cursor()
    create_table_department = 'CREATE TABLE DEPARTMENT (ID INT PRIMARY KEY NOT NULL, NAME TEXT, LOCATION TEXT);'
    create_table_employee = 'CREATE TABLE EMPLOYEE (ID INT PRIMARY KEY NOT NULL, NAME TEXT, SALARY INT, DEPT_ID INT REFERENCES DEPARTMENT (ID));'
    cursor.execute(create_table_department)
    connection.commit()
    cursor.execute(create_table_employee)
    connection.commit()

    insert_department = "INSERT INTO DEPARTMENT (ID, NAME, LOCATION) VALUES (1, 'Executive', 'Sydney'), (2, 'Production', 'Sydney'), (3, 'Resources', 'Cape Town'), (4, 'Technical', 'Texas'), (5, 'Management', 'Paris');"
    insert_employee = "INSERT INTO EMPLOYEE (ID, NAME, SALARY, DEPT_ID) VALUES (1, 'Candice', 4685, 1), (2, 'Julia', 2559, 2), (3, 'Bob', 4405, 4), (4, 'Scarlet', 2350, 1), (5, 'Ileana', 1151, 4);"
    cursor.execute(insert_department)
    connection.commit()
    cursor.execute(insert_employee)
    connection.commit()

    select_result = "SELECT DEPARTMENT.NAME, S.CNT FROM DEPARTMENT JOIN (SELECT D.ID AS ID, COUNT(E.ID) AS CNT FROM DEPARTMENT D JOIN EMPLOYEE E ON E.DEPT_ID = D.ID GROUP BY D.ID) S ON S.ID = DEPARTMENT.ID ORDER BY S.CNT DESC, DEPARTMENT.NAME"
    cursor.execute(select_result)
    result = cursor.fetchall()
    print("Result:\n", result)

