import sqlite3
import os

def db():
  # Connect to the database
  db_dir = os.path.join(os.getcwd(), 'db')
  if not os.path.exists(db_dir):
      os.makedirs(db_dir)

  db_path = os.path.join(db_dir, 'db.db')
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()

  # Create the products table
  cursor.execute("""CREATE TABLE IF NOT EXISTS products (
      id INTEGER PRIMARY KEY,
      name TEXT,
      price REAL,
      quantity INTEGER,
      barcode INTEGER
  )""")

  # Create the sales table
  cursor.execute("""CREATE TABLE IF NOT EXISTS sales (
      id INTEGER PRIMARY KEY,
      sale_value REAL,
      quantity INTEGER,
      customer_name TEXT,
      product TEXT,
      sale_number INTEGER
  )""")

  # Commit the changes and close the connection
  conn.commit()
  cursor.close()
  conn.close()
