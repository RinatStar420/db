import sqlalchemy as sa
conn = sa.create_engine('sqlite:///books.db')
rows = conn.execute('SELECT title FROM books ORDER BY title')
for row in rows:
    print(row)