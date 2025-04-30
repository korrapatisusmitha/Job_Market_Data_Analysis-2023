import psycopg2
from db_config import DB_CONFIG

def get_db_connection():
    return psycopg2.connect(
        host = DB_CONFIG['host'],
        port = DB_CONFIG['port'],
        dbname = DB_CONFIG['database'],
        user = DB_CONFIG['user'],
        password = DB_CONFIG['password']
    )

    
