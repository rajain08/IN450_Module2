import psycopg2

class DataLayer:

    def __init__(self, db_name="postgres", user="postgres", password="TTGSKA1R", host="localhost"):
        self.conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host)

    def get_data(self, table_name):
        """
        Fetches data from a specified table.

        Args:
            table_name (str): Name of the table to fetch data from.

        Returns:
            list: List of rows from the table.
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        cursor.close()
        return data

    def get_row_count(self, table_name):
        """
        Counts the number of rows in a specified table.

        Args:
            table_name (str): Name of the table to count rows.

        Returns:
            int: Number of rows in the table.
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        cursor.close()
        return count

    def close_connection(self):
        """
        Closes the connection to the database.
        """
        self.conn.close()