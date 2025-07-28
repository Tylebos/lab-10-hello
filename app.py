from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Tyler Bosford in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://basketball_names_user:coWuQ7WjVRtH4r9uhIEdsC0Rdac7hDTo@dpg-d23lqpvdiees739os0og-a.oregon-postgres.render.com/basketball_names")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://basketball_names_user:coWuQ7WjVRtH4r9uhIEdsC0Rdac7hDTo@dpg-d23lqpvdiees739os0og-a.oregon-postgres.render.com/basketball_names")
    cur = conn.cursor()
    # Create a table with Columns first, last, city, name, number
    cur.execute('''
    CREATE TABLE IF NOT EXISTS
    Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Table created successfully"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://basketball_names_user:coWuQ7WjVRtH4r9uhIEdsC0Rdac7hDTo@dpg-d23lqpvdiees739os0og-a.oregon-postgres.render.com/basketball_names")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leanord', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated Successfully"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgresql://basketball_names_user:coWuQ7WjVRtH4r9uhIEdsC0Rdac7hDTo@dpg-d23lqpvdiees739os0og-a.oregon-postgres.render.com/basketball_names")
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    # Create HTML from records
    response_string = "<table border='1'>"
    for player in records:
        response_string += "<tr>"
        for data in player:
            response_string += "<td>{}</td>".format(data)
        response_string += "</tr>"
    response_string += "</table>"
    return response_string

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect("postgresql://basketball_names_user:coWuQ7WjVRtH4r9uhIEdsC0Rdac7hDTo@dpg-d23lqpvdiees739os0og-a.oregon-postgres.render.com/basketball_names")
    cur = conn.cursor()
    cur.execute('''
    DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Dropped"