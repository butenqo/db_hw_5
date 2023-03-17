import psycopg2




def create_db(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS client(
            client_id INTEGER PRIMARY KEY,  
            name VARCHAR ,
            last_name VARCHAR,
            email VARCHAR );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phone_number(
            phone_number INTEGER PRIMARY KEY,
            client_id INTEGER REFERENCES client(client_id));
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
    
    sql = '''UPDATE client SET
            name = COALESCE(%s, name),
            last_name = COALESCE(%s, last_name),
            email = COALESCE(%s, email) WHERE
            client_id = COALESCE(%s, client_id)'''
    cur.execute(sql, (name, last_name, email, client_id))

    

def delete_phone_number(cur, phone_number):
    cur.execute("""
    DELETE FROM phone_number WHERE phone_number = %s;
    """, ([phone_number]))
    


def delete_client(cur, client_id):
    cur.execute("""
    DELETE FROM client WHERE client_id = %s;
    """, ([client_id]))
    

def find_client(cur,  name=None, last_name= None, email = None, phone_number = None):
    
    if phone_number == None:
        sql = '''SELECT * FROM client
                WHERE name = COALESCE(%s, name)
                and last_name = COALESCE(%s, last_name)
                and email = COALESCE(%s, email)
                '''
        cur.execute(sql ,(name, last_name, email))
    else:
        sql = '''SELECT * FROM client
                JOIN phone_number on client.client_id = phone_number.client_id
                WHERE name = COALESCE(%s, name)
                and last_name = COALESCE(%s, last_name)
                and email = COALESCE(%s, email)
                and phone_number = COALESCE(%s, phone_number)'''
        cur.execute(sql ,(name, last_name, email, phone_number))
    print(cur.fetchall())

if __name__ == "__main__":
    with psycopg2.connect(database="clients_db", user="postgres", password="") as conn:
        with conn.cursor() as cur:
            pass
conn.close()