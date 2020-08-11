import psycopg2


def db_connector():
    pass


def query_handler(db_conn, query, action):
    pass


db_connect = psycopg2.connect(database = 'online_ticket', user= 'ashkan',
                                password = '1234', host = 'localhost', port = '5432')


my_cursor = db_connect.cursor()

print('connect to db successfully!')

# query = "SELECT * FROM accounts WHERE username LIKE 'a_%';"
# query = "SELECT (username , pass) FROM accounts"
# query = '''CREATE TABLE profile(profile_id serial PRIMARY KEY,
#             user_name INT
#             REFERENCES accounts(user_id) ON DELETE 
#             SET NULL);
#         '''

# ALTER TABLE profile DROP CONSTRAINT profile_user_name_fkey;
# ALTER TABLE profile DROP COLUMN user_name;
# ALTER TABLE profile ADD CONSTRAINT profile_user_name_fkey FOREIGN KEY (user_name) REFERENCES accounts(username) ON DELETE CASCADE;
# ALTER TABLE profile ADD COLUMN user_name VARCHAR(50) UNIQUE;
# UPDATE profile SET user_name = 'ali_zafar' WHERE profile_id = 2;
# DELETE FROM profile WHERE profile_id = 2;
# records = my_cursor.fetchall()

# SELECT * FROM profile INNER JOIN accounts ON profile.user_name = accounts.username;
# SELECT * FROM profile LEFT JOIN accounts ON profile.user_name = accounts.username;
# SELECT * FROM profile LEFT OUTER JOIN accounts ON profile.user_name = accounts.username WHERE profile.user_name ISNULL;


db_connect.commit()

db_connect.close()
'''
for record in records:
    print(record[0])
'''

# INSERT INTO profile(user_name) VALUES((SELECT user_id from accounts WHERE username='ali_zafar'));