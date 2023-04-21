import numpy as np 
from AutoTable.elements import Elements as E

class Table: 
    def __init__(self, table_columns) -> None:

        self.table_columns = table_columns
        self.table_elements = []


    def make_errorbar_value(self, column, round_digits=3):
        operation_data = np.asarray(self.source_data[column])
        val = np.round(operation_data.mean(), round_digits)
        errorbar = np.round(operation_data.std(), round_digits)

        return f"{val}$\pm${errorbar}"

    def add_hline(self): 
        self.table_elements.append("\\hline")

    def add_multirow_element(self, super_rows, rows, fill_data, add_hlines=True):
        for row, subtable_data in zip(super_rows, fill_data): 
            self.table_elements.append(f"\\multirow*[{row}]")
            row_element = E.mutlirow_subtable(rows, data_to_fill=subtable_data)
            for element in row_element: 
                self.table_elements.append(element)
            if add_hlines: 
                self.add_hline()

    def add_multicol_element(self, super_columns, columns, title, rows_name, data_to_fill):
        rows = E.multicol_subtable(super_columns, columns, title, rows_name, data_to_fill)
        for row in rows: 
            self.table_elements.append(row)

    def make(self): 
        self.table_elements.insert(0, E.single_row(self.table_columns))
        self.table_elements.insert(0, f"\\begin{{tabular}}[{'|'.join('l' for _ in range(len(self.table_columns)))}]")
        self.table_elements.insert(0, "\\begin{table}")

        self.table_elements.append("\\label{}")
        self.table_elements.append("\\end{tabular}")
        self.table_elements.append("\\end{table}")

        table = E.joined_rows(self.table_elements)
        table = E.replace_braces(table)

        print(table)
        return table



