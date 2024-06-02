from tkinter import Tk, Label, Button, Text
from business_layer import BusinessLayer

class DisplayData:

    def __init__(self):
        self.root = Tk()
        self.root.title("Database Data Viewer")

        self.business_layer = BusinessLayer()

        self.in450a_label = Label(self.root, text="Table IN450A Data:")
        self.in450a_label.pack()
        self.in450a_text = Text(self.root, width=100, height=10)
        self.in450a_text.pack()

        self.in450b_label = Label(self.root, text="Table IN450B Data:")
        self.in450b_label.pack()
        self.in450b_text = Text(self.root, width=100, height=10)
        self.in450b_text.pack()

        self.count_button = Button(self.root, text="Get Table IN450A Row Count", command=self.get_row_count)
        self.count_button.pack()

        self.names_button = Button(self.root, text="Get Table IN450B Names", command=self.get_names)
        self.names_button.pack()

        self.display_data()
        self.root.mainloop()

    def display_data(self):
        """
        Displays data from in450a and in450b tables in their respective Text widgets.
        """
        in450a_data = self.business_layer.get_in450a_data()
        self.in450a_text.delete(1.0, 'end')
        for row in in450a_data:
            self.in450a_text.insert('end', f"{row}\n")

        in450b_data = self.business_layer.get_in450b_data()
        self.in450b_text.delete(1.0, 'end')
        for row in in450b_data:
            self.in450b_text.insert('end', f"{row}\n")

    def get_row_count(self):
        """
        Fetches and displays the number of rows in the in450a table.
        """
        count = self.business_layer.get_in450a_row_count()
        message = f"Number of rows in in450a: {count}"
        self.in450a_text.delete(1.0, 'end')
        self.in450a_text.insert('end', message)

    def get_names(self):
        """
        Fetches and displays a list of first and last names from the in450b table.
        """
        names = self.business_layer.get_in450b_names()
        self.in450b_text.delete(1.0, 'end')
        for name in names:
            self.in450b_text.insert('end', f"{name}\n")


if __name__ == "__main__":
    gui = DisplayData()