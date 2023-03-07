import sqlite3
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect('guestbook.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts ORDER BY id DESC')
    posts = cursor.fetchall()
    conn.close()
    return render_template('guestbook.html', posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form['name']
        message = request.form['message']
        title = request.form['title']
        conn = sqlite3.connect('guestbook.db')
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO posts (title, author, content) VALUES (?, ?, ?)', (title, author, message))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run()

"""
create a database 
sqlite3 guestbook.db


"""
