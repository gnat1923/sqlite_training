import sqlite3

''' UPDATE 1 COL
sql = "UPDATE tasks SET priority = ? WHERE id = ?"

try:
    with sqlite3.connect("my.db") as conn:
        cur = conn.cursor()
        cur.execute(sql, (2,1))
        conn.commit

except sqlite3.Error as e:
    print(e)'''

#update multiple columns
sql = "UPDATE tasks SET priority = ?, status_id = ? WHERE id = ?"

try:
    with sqlite3.connect("my.db") as conn:
        cur = conn.cursor()
        cur.execute(sql, (3,2,1))
        conn.commit()
        print('Update successful')

except sqlite3.Error as e:
    print(e)