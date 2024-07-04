import psycopg2

database_url = "dbname=dsp host=192.168.1.140 port=7000 user=postgres password=postgres"

def get_connection_object(connection_string):
    return psycopg2.connect(connection_string)

def get_db_response(query, connection_string):
    connection = get_connection_object(connection_string)
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

