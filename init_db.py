import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS games;')
cur.execute('CREATE TABLE games (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'publisher varchar (50) NOT NULL,'
                                 'hours_num integer NOT NULL,'
                                 'completed text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO games (title, publisher, hours_num, completed)'
            'VALUES (%s, %s, %s, %s)',
            ('Elden Ring',
             'From Software',
             300,
             'Finished several times!')
            )


cur.execute('INSERT INTO games (title, publisher, hours_num, completed)'
            'VALUES (%s, %s, %s, %s)',
            ('The Legend of Heroes: Trails of Cold Steel II',
             'XSEED',
             90,
             'At the final boss.')
            )

conn.commit()

cur.close()
conn.close()
