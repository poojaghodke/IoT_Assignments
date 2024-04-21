import dbcon

def update_employees(id,de,sa):
    
    connection = dbcon.get_connection()
    
    query = f"update employees SET dept =%s, salary=%s dateofjoin=%s where empid=%s;"
    val = (de,sa,id)
    cursor = connection.cursor()

    cursor.execute(query, val)
    connection.commit()
    cursor.close()
    connection.close()