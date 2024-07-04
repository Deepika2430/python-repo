import psycopg2

def get_connection_object(connection_string):
    return psycopg2.connect(connection_string)

def get_db_response(query, connection_string):
    connection = get_connection_object(connection_string)
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

