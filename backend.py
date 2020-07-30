import sqlite3


class Database:


    def __init__(self, db):
        self.conn = sqlite3.connect("books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, ISBN integer)")
        self.conn.commit()


    def insert(self, title, author, year, ISBN):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, ISBN))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows


    def search(self, title="", author="", year="", ISBN=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR ISBN=? ", (title, author, year, ISBN))
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows


    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()


    def update(self, id,title, author, year, ISBN):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, ISBN=? WHERE id=?",(title, author, year, ISBN, id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()


#insert("The ssun", "John Smith", 1918, 91312121)
#delete(3)
#update(4, "The SUN", "John Samonta", 2020, 99999999)
#print(view())
#print(search(author="John Smith"))