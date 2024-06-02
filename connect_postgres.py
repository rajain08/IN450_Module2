import psycopg2

# Database connection parameters
dbname = "postgres"
user = "postgres"
password = "TTGSKA1R"
host = "localhost"  # Change if your database is hosted elsewhere
port = 5432  # Default port for PostgreSQL

# Connect to the database
try:
  conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
  print("Connection established successfully!")
except psycopg2.Error as e:
  print("Error connecting to database:", e)

# Close the connection (optional, will be closed automatically with 'with' block)
if conn:
  conn.close()
  print("Connection closed.")

# Using a 'with' block for automatic connection closing (recommended)
with psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port) as conn:
  print("Connection established using 'with' block!")