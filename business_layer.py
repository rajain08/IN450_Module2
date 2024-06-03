from data_layer import DataLayer

class BusinessLayer:

    def __init__(self, server, database, user, password):
        self.data_layer = DataLayer(host=server, db_name=database, user=user, password=password)

    def get_in450a_row_count(self):
        return self.data_layer.get_row_count("in450a")

    def get_in450b_names(self):
        data = self.data_layer.get_data("in450b")
        names = [(row[0], row[1]) for row in data]
        return names

    def get_in450c_row_count(self):
        return self.data_layer.get_row_count("in450c")

    def get_in450a_data(self):
        """
        Fetches all data from the IN450a table.
        """
        return self.data_layer.get_data("in450a")

    def get_in450b_data(self):
        """
        Fetches all data from the IN450b table.
        """
        return self.data_layer.get_data("in450b")

    def get_in450c_data(self):
        """
        Fetches all data from the IN450c table.
        """
        return self.data_layer.get_data("in450c")
