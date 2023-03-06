import psycopg2

conn = psycopg2.connect(database="clients_db", user="postgres", password="215047Qq")


def create_db(cur):
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
        
def add_client(cur, client_id, name, last_name, email):
    cur.execute("""
        INSERT INTO client VALUES (%s, %s, %s, %s);
        """, (client_id, name, last_name, email))
   

def add_phone_number(cur, phone_number, client_id):
    cur.execute("""
        INSERT INTO phone_number VALUES (%s, %s);
        """, (phone_number, client_id))



def update_client(cur, client_id, name=None, last_name=None, email=None):
    cur.execute("""
    UPDATE client SET client_id=%s, name=%s, last_name=%s, email=%s;
    """, (client_id, name, last_name, email))
    

def delete_phone_number(cur, phone_number):
    cur.execute("""
    DELETE FROM phone_number WHERE phone_number = %s;
    """, ([phone_number]))
    


def delete_client(cur, client_id):
    cur.execute("""
    DELETE FROM client WHERE client_id = %s;
    """, ([client_id]))
    

def find_client(cur, **kwargs):
    name = kwargs['name']
    last_name = kwargs['last_name']
    email= kwargs['email']
   
    cur.execute("""
    SELECT * FROM client WHERE client_id = %s AND name=%s AND last_name=%s AND email=%s;""",(name, last_name, email))
    print(cur.fetchall())

if __name__ == "__main__":
    with psycopg2.connect(database="clients_db", user="postgres", password="215047Qq") as conn:
        with conn.cursor() as cur:
            pass
            
conn.close()