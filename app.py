from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Tyler Bosford in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://basketball_names_user:coWuQ7WjVRtH4r9uhIEdsC0Rdac7hDTo@dpg-d23lqpvdiees739os0og-a/basketball_names")
    
