import sqlite3

def connect():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("create table if not exists books(id INTEGER PRIMARY KEY AUTOINCREMENT ,title varchar(100),author varchar(100),year int,ISBN int)")  
    conn.commit()
    conn.close()
    
def insert(title,author,year,isbn):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("Insert into books values (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
    view()

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("select *from books")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("select *from books where title = ? or author =? or year = ? or isbn = ?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows  


def delete(id):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("delete from books where id = ?",(id,))
    conn.commit()
    conn.close()
    
def update(id,title,author,year,isbn):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("update books set title =?, author =?,year =?,isbn =? where id =?",(id,title,author,year,isbn))
    conn.commit()
    conn.close()
    

connect()
print(view())
