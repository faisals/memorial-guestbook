import sqlite3

connection = sqlite3.connect('guestbook.db')

"""read a sql file and execute it"""
with open("schema.sql") as f:
    connection.executescript(f.read())


"""with open('schema.sql') as f:
    connection.executescript(f.read())
"""

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, author, content) VALUES (?, ?, ?)",
            ('Will miss you friend', 'Faisal', 'I will miss you friend.')
            )

cur.execute("INSERT INTO posts (title, author, content) VALUES (?, ?, ?)",
            ('Faithful departed', 'Resha', 'I will miss you friend.')
            )

cur.execute("INSERT INTO posts (author, title, content) VALUES (?, ?, ?)",
            ('Alex Chen', 'Rest easy, my friend', 'You fought a brave battle and inspired us all.'))
cur.execute("INSERT INTO posts (author, title, content) VALUES (?, ?, ?)",
            ('Bob Johnson', 'In loving memory', 'You touched so many lives with your kindness and generosity.'))
cur.execute("INSERT INTO posts (author, title, content) VALUES (?, ?, ?)",
            ('David Brown', 'Forever in our hearts', 'We will honor your legacy and keep your memory alive.'))
cur.execute("INSERT INTO posts (author, title, content) VALUES (?, ?, ?)",
            ('Emily Wang', 'Thank you for everything', 'You made the world a better place and touched so many lives.'))
cur.execute("INSERT INTO posts (author, title, content) VALUES (?, ?, ?)",
            ('Jane Doe', 'Rest in peace', 'You will be missed, but never forgotten.'))
cur.execute("INSERT INTO posts (author, title, content) VALUES (?, ?, ?)",
            ('John Smith', 'Farewell, my friend', 'I will always cherish the memories we shared.'))
cur.execute("INSERT INTO posts (author, title, content) VALUES (?, ?, ?)",
            ('Karen Kim', 'Goodbye for now', 'I know we will meet again someday.'))
cur.execute("INSERT INTO posts (author, title, content) VALUES (?, ?, ?)",
            ('Mike Davis', 'Until we meet again', 'I will always remember your smile and your laughter.'))
cur.execute("INSERT INTO posts (author, title, content) VALUES (?, ?, ?)",
            ('Rachel Kim', 'In our thoughts and prayers', 'We send our love and condolences to your family.'))
cur.execute("INSERT INTO posts (author, title, content) VALUES (?, ?, ?)",
            ('Samantha Lee', 'Gone too soon', 'You had so much more to give, but your spirit will live on.'))


connection.commit()
connection.close()
