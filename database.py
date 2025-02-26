import sqlite3

DB_NAME = "tasks.db"

def init_db():
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed BOOLEAN DEFAULT 0,
    date_added DATE DEFAULT CURRENT_DATE
  )
  """)

  conn.commit()
  conn.close()

def get_db_connection():
  """Creates and returns a connection"""
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  return conn, cursor

def add_task(task):
  conn, cursor = get_db_connection()
  cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
  conn.commit()
  conn.close()

def get_tasks():
  conn, cursor = get_db_connection()
  cursor.execute("SELECT * FROM tasks ORDER BY rowid ASC")
  tasks = cursor.fetchall()
  conn.close()
  return tasks

def update_task(task_id, new_task_text):
  conn, cursor = get_db_connection()
  cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (new_task_text, task_id,))
  conn.commit()
  conn.close()

def delete_task(task_id):
  conn, cursor = get_db_connection()
  cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
  conn.commit()
  conn.close()

def toggle_completed(task_id):
  conn, cursor = get_db_connection()
  cursor.execute("SELECT completed FROM tasks WHERE id = ?", (task_id,))
  current_status = cursor.fetchone()[0]
  new_status = 0 if current_status else 1
  cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (new_status, task_id))
  conn.commit()
  conn.close()