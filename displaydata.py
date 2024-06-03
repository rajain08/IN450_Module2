from tkinter import Tk, Label, Button, Text, Entry, messagebox, END
from business_layer import BusinessLayer
import psycopg2

class DisplayData:

    def __init__(self):
        self.root = Tk()
        self.root.title("Database Data Viewer")

        # Login section
        self.server_label = Label(self.root, text="Server:")
        self.server_label.pack()
        self.server_entry = Entry(self.root)
        self.server_entry.pack()

        self.database_label = Label(self.root, text="Database:")
        self.database_label.pack()
        self.database_entry = Entry(self.root)
        self.database_entry.pack()

        self.user_label = Label(self.root, text="Username:")
        self.user_label.pack()
        self.user_entry = Entry(self.root)
        self.user_entry.pack()

        self.password_label = Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack()

        self.login_button = Button(self.root, text="Login", command=self.login)
        self.login_button.pack()

        # Data display section (initially hidden)
        self.data_text = Text(self.root, width=100, height=10)
        self.data_text.pack_forget()

        self.count_button_a = Button(self.root, text="IN450a Row Count", command=self.get_in450a_count)
        self.count_button_a.pack_forget()

        self.names_button_b = Button(self.root, text="IN450b Names", command=self.get_in450b_names)
        self.names_button_b.pack_forget()

        self.count_button_c = Button(self.root, text="IN450c Row Count", command=self.get_in450c_count)
        self.count_button_c.pack_forget()

        self.view_data_a_button = Button(self.root, text="View IN450a Data", command=self.get_in450a_data)
        self.view_data_a_button.pack_forget()

        self.view_data_b_button = Button(self.root, text="View IN450b Data", command=self.get_in450b_data)
        self.view_data_b_button.pack_forget()

        self.view_data_c_button = Button(self.root, text="View IN450c Data", command=self.get_in450c_data)
        self.view_data_c_button.pack_forget()

        self.root.mainloop()

    def login(self):
        """
        Attempts to login with provided credentials and enables data access based on role.
        """
        server = self.server_entry.get()
        database = self.database_entry.get()
        user = self.user_entry.get()
        password = self.password_entry.get()

        try:
            self.business_layer = BusinessLayer(server, database, user, password)
            self.show_data_section()
            self.login_button.config(state="disabled")
        except (psycopg2.OperationalError, psycopg2.InterfaceError) as e:
            messagebox.showerror("Error", f"Login failed: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def show_data_section(self):
        """
        Shows the data display section and enables buttons based on user role.
        """
        self.data_text.pack()
        user = self.user_entry.get()
        if user == "in450a":
            self.count_button_a.pack()
            self.names_button_b.pack()
            self.count_button_c.pack()
            self.view_data_a_button.pack()
            self.view_data_b_button.pack()
            self.view_data_c_button.pack()
        elif user == "in450b":
            self.names_button_b.pack()
            self.view_data_b_button.pack()
        elif user == "in450c":
            self.count_button_c.pack()
            self.view_data_c_button.pack()
        else:
            messagebox.showerror("Error", "Invalid role. Access denied.")

    def get_in450a_count(self):
        """
        Fetches and displays the number of rows in the in450a table.
        """
        try:
            count = self.business_layer.get_in450a_row_count()
            self.data_text.delete(1.0, 'end')
            self.data_text.insert(1.0, f"IN450a Row Count: {count}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve IN450a row count: {e}")

    def get_in450b_names(self):
        """
        Fetches and displays first and last names from the IN450b table.
        """
        try:
            names = self.business_layer.get_in450b_names()
            self.data_text.delete(1.0, 'end')

            if names:
                for name in names:
                    self.data_text.insert(END, f"{name[0]} {name[1]}\n")
            else:
                self.data_text.insert(1.0, "No names found in IN450b table.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve names from IN450b: {e}")

    def get_in450c_count(self):
        """
        Fetches and displays the number of rows in the in450c table.
        """
        try:
            count = self.business_layer.get_in450c_row_count()
            self.data_text.delete(1.0, 'end')
            self.data_text.insert(1.0, f"IN450c Row Count: {count}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve IN450c row count: {e}")

    def get_in450a_data(self):
        """
        Fetches and displays all data from the IN450a table.
        """
        try:
            data = self.business_layer.get_in450a_data()
            self.data_text.delete(1.0, 'end')

            if data:
                for row in data:
                    self.data_text.insert(END, f"{row}\n")
            else:
                self.data_text.insert(1.0, "No data found in IN450a table.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve IN450a data: {e}")

    def get_in450b_data(self):
        """
        Fetches and displays all data from the IN450b table.
        """
        try:
            data = self.business_layer.get_in450b_data()
            self.data_text.delete(1.0, 'end')

            if data:
                for row in data:
                    self.data_text.insert(END, f"{row}\n")
            else:
                self.data_text.insert(1.0, "No data found in IN450b table.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve IN450b data: {e}")

    def get_in450c_data(self):
        """
        Fetches and displays all data from the IN450b table.
        """
        try:
            data = self.business_layer.get_in450c_data()
            self.data_text.delete(1.0, 'end')

            if data:
                for row in data:
                    self.data_text.insert(END, f"{row}\n")
            else:
                self.data_text.insert(1.0, "No data found in IN450c table.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve IN450c data: {e}")

if __name__ == "__main__":
    gui = DisplayData()
