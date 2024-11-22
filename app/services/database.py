import pyodbc
from config.settings import DATABASE_CONFIG

def get_database_connection():
    conn_str = ";".join(f"{key}={value}" for key, value in DATABASE_CONFIG.items())
    return pyodbc.connect(conn_str)

def get_database_schema():
    conn = get_database_connection()
    cursor = conn.cursor()
    query = """
        SELECT TABLE_NAME, COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        ORDER BY TABLE_NAME, ORDINAL_POSITION;
    """
    cursor.execute(query)
    schema = cursor.fetchall()
    conn.close()

    schema_dict = {}
    for table, column in schema:
        schema_dict.setdefault(table, []).append(column)
    return schema_dict

def fetch_data(query):
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows
