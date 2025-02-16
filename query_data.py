import sqlite3

try:
    with sqlite3.connect("my.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name, priority FROM tasks")
        rows = cur.fetchall()

        for row in rows:
            print(row)

        print('List task names only')
        for row in rows:
            print(row[1])

except sqlite3.OperationalError as e:
    print(e)