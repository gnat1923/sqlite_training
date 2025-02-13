import sqlite3

def add_project(conn, project):
    #insert table statement
    sql = '''INSERT INTO projects(name, begin_date, end_date)
            VALUES(?,?,?)'''
    
    #create cursor
    cur = conn.cursor()

    #execute INSERT statement
    cur.execute(sql, project)

    #commit changes
    conn.commit()

    #get id of created project
    return cur.lastrowid

def add_task(conn, task):
    sql = '''INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
             VALUES(?,?,?,?,?,?)'''
    
    cur = conn.cursor()

    cur.execute(sql, task)
    
    conn.commit()

    return cur.lastrowid

def main():
    try:
        with sqlite3.connect("my.db") as conn:
            #add a project
            project = ('Cool App with SQLite & Python', '2025-02-13', '2025-03-13')
            project_id = add_project(conn, project)
            print(f"Created a project with the id {project_id}")

            #add a task
            tasks = [
                ('Analyse the requirements of the app', 1, 1, project_id, '2025-02-13', '2025-02-14' ),
                ('Confirm with user about top requirements', 1, 1, project_id, '2025-02-15', '2025-02-18' )
            ]

            for task in tasks:
                task_id = add_task(conn, task)
                print(f"Created task with id {task_id}")


    except sqlite3.Error as e:
        print(e)

if __name__ == "__main__":
    main()