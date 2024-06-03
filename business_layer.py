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
