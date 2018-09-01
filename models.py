import sqlite3 as sql 
from os import path

root = path.dirname(path.realpath(__file__))

def create_post(name, content, time):
    con = sql.connect(path.join(root, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content, time) values(?,?,?)', (name, content, time))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(root, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts

def clear_posts():
    con = sql.connect(path.join(root, 'database.db'))
    cur = con.cursor()
    cur.execute('delete from posts')
    con.commit()
    con.close()