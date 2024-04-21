import dbcon

def delete_employees(empid):
    connection = dbcon.get_connection()
    query = f"delete from employees where empid = %s;"
    val = (empid, )

    cursor = connection.cursor()

    cursor.execute(query, val)

    connection.commit()
    cursor.close()
    connection.close()
