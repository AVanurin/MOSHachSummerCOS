import sqlite3

DB_PATH = "db.sqlite3"

def connect():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    return con, cur


def iinit_db():
    print("Начало переустановки базы данных в", DB_PATH)
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    f = open("Shema.sql")
    script = f.read()
    f.close()

    cursor.executescript(script)
    
    connection.commit()
    connection.close()
    print("База данных была успешно инициализирована по схеме")

def all_tasks():
    connecton = sqlite3.connect(DB_PATH)
    cursor = connecton.cursor()

    cwd = """
    SELECT * FROM tasks;
    """
    cursor.execute(cwd)
    results = cursor.fetchall()
    connecton.close()

    return results

def task(Id: int):
    connection, cursor = connect()

    cwd  = f"""
    SELECT * FROM tasks WHERE id={Id};
    """
    cursor.execute(cwd)
    results = cursor.fetchone()
    connection.close()

    return results

def new_task(sender: str, text: str, status: int):
    connection, cursor = connect()

    cwd = f"""
    INSERT INTO tasks(
        sender,
        text,
        status
    ) VALUES (?, ?, ?);
    """

    cursor.execute(cwd, (sender, text, status))
    connection.commit()
    last = cursor.lastrowid()

    connection.close()
    return last

def change_task_status(Id: int, new_status: int):
    connection, cursor = connect()

    cwd = f"""
    UPDATE tasks SET status={new_status}  WHERE id=ID;
    """

    cursor.execute(cwd)
    connection.commit()

    connection.close()

    return 0

def solution(for_id: int):
    connection, cursor = connect()

    cwd = f"""
    SELECT * FROM solutions WHERE task_id={for_id}
    """

    cursor.execute(cwd)
    result = cursor.fetchone()
    connection.close()
    return result

def add_solution(for_id: int, text: str):
    connection, cursor = connect()

    cwd = """
    INSERT INTO solutions(
        task_id,
        text
    ) VALUES (?, ?);
    """

    cursor.execute(cwd, (for_id, text))
    connection.commit()
    last = cursor.lastrowid

    connection.close()
    return last

if __name__ == "__main__":
    iinit_db()
    print(all_tasks())