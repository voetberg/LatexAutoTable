class Elements: 
    @staticmethod
    def mutlirow_subtable(multirow_headers, data_to_fill):
        rows = []
        for row_index, row_header in enumerate(multirow_headers):
            data_fill = list(data_to_fill[row_index])
            data_fill.insert(0, f"& {row_header.strip('_')}")
            rows.append(Elements.single_row(data_fill))

        return rows
    
    @staticmethod
    def singlerow_subtable(data_to_fill):
        rows = []
        for row in data_to_fill:
            data_fill = list(row)
            rows.append(Elements.single_row(data_fill))

        return rows

    @staticmethod
    def multicol_subtable(super_columns, columns, title, rows_name, data_to_fill):
        column_headers = [
            f"\\multicolumn[2][c][{column}]" for column in super_columns
        ]

        row_header = f"\\multirow{{2}}{{*}}[{title}]"
        column_headers.insert(0, row_header)

        super_header = Elements.single_row(column_headers)
        super_header = Elements.replace_braces(super_header)

        header = Elements.single_row(columns)
        table = [header]

        for row, name in zip(data_to_fill, rows_name): 
            data_fill = list(row)
            data_fill.insert(0, f"& {name.strip('_')}")
            table.append(Elements.single_row(data_fill))
        
        return table

    @staticmethod
    def joined_rows(rows): 
        return " \\\\ \n".join(rows)

    @staticmethod
    def replace_braces(joined_row): 
        return joined_row.replace("[", "{").replace("]", "}")

    @staticmethod
    def single_row(data_to_fill): 
        return " & ".join(map(str, data_to_fill))
