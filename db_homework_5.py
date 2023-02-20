import psycopg2


def create_db(conn):
      with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS client(
                client_id VARCHAR PRIMARY KEY,  
                name VARCHAR ,
                last_name VARCHAR,
                email VARCHAR );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phone_number(
                phone_number INTEGER PRIMARY KEY,
                client_id VARCHAR REFERENCES client(client_id));
        """)
        
        conn.commit()

def add_client(conn, client_id, name, last_name, email):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO client VALUES (%s, %s, %s, %s);
            """, (client_id, name, last_name, email))
    conn.commit()

def add_phone_number(conn, phone_number, client_id):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO phone_number VALUES (%s, %s);
            """, (phone_number, client_id))
    conn.commit()


def update_client(conn, client_id, name=None, last_name=None, email=None):
    with conn.cursor() as cur:
        cur.execute("""
         UPDATE client SET client_id=%s, name=%s, last_name=%s, email=%s;
        """, (client_id, name, last_name, email))
    conn.commit()

def delete_phone_number(conn, phone_number):
    with conn.cursor() as cur:
        cur.execute("""
         DELETE FROM phone_number WHERE phone_number = %s;
        """, ([phone_number]))
    conn.commit()


def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""
         DELETE FROM client WHERE client_id = %s;
        """, ([client_id]))
    conn.commit()

def find_client(conn, client_id=None, name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT * FROM client WHERE client_id = %s OR name=%s OR last_name=%s OR email=%s;
        """, (client_id, name, last_name, email))
        print(cur.fetchall())

with psycopg2.connect(database="clients_db", user="postgres", password="") as conn:  
    