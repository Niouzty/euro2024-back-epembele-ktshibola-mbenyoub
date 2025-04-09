class Table:
    def __init__(self, table_name: str, columns: list):
        self.table_name = table_name
        self.columns = columns

    def to_dict(self):
        return {
            'table_name': self.table_name,
            'columns': self.columns
        }
