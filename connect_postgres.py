import psycopg2

dbname = "postgres"
user = "postgres"
password = "TTGSKA1R"
host = "localhost"
port = 5432

try:
  conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
  print("Connection established successfully!")
except psycopg2.Error as e:
  print("Error connecting to database:", e)

if conn:
  conn.close()
  print("Connection closed.")

with psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port) as conn:
  print("Connection established using 'with' block!")
