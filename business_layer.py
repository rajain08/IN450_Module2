from data_layer import DataLayer

class BusinessLayer:

    def __init__(self):
        self.data_layer = DataLayer()

    def get_in450a_data(self):
        """
        Returns data from the in450a table.

        Returns:
            list: List of rows from in450a table.
        """
        return self.data_layer.get_data("in450a")

    def get_in450b_data(self):
        """
        Returns data from the in450b table.

        Returns:
            list: List of rows from in450b table.
        """
        return self.data_layer.get_data("in450b")

    def get_in450a_row_count(self):
        """
        Returns the number of rows in the in450a table.

        Returns:
            int: Number of rows in in450a.
        """
        return self.data_layer.get_row_count("in450a")

    def get_in450b_names(self):
        """
        Returns a list of first and last names from in450b.

        Returns:
            list: List of tuples containing (first_name, last_name).
        """
        data = self.data_layer.get_data("in450b")
        names = [f"{row[0]} {row[1]}" for row in data]
        return names
