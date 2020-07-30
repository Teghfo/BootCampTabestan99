import psycopg2


def db_connector():
    pass


def query_handler(db_conn, query):
    pass
query


db_connect = psycopg2.connect(database = 'online_ticket', user= 'ashkan',
                                password = '1234', host = 'localhost', port = '5432')


my_cursor = db_connect.cursor()

print('connect to db successfully!')

# query = "SELECT * FROM accounts WHERE username LIKE 'a_%';"
# query = "SELECT (username , pass) FROM accounts"
query = '''CREATE TABLE profile(profile_id serial PRIMARY KEY,
            user_name INT
            REFERENCES accounts(user_id) ON DELETE 
            SET NULL);
        '''

my_cursor.execute(query)

# records = my_cursor.fetchall()
db_connect.commit()

db_connect.close()
'''
for record in records:
    print(record[0])
'''

# INSERT INTO profile(user_name) VALUES((SELECT user_id from accounts WHERE username='ali_zafar'));