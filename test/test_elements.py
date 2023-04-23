import sys 
sys.path.append("..")

from AutoTable.elements import Elements as E
import numpy as np
import pytest 


def test_single_row(): 
    data_fill = np.zeros(2)
    expected_str = "0.0 & 0.0"
    element = E.single_row(data_fill)
    assert expected_str == element

def test_singlerow_table(): 
    data_fill = np.zeros((2,2))
    expected_table = [
        "0.0 & 0.0", "0.0 & 0.0"
    ]
    table_contents = E.singlerow_subtable(data_fill)

    assert expected_table == table_contents

def test_joined_table():
    current_table = [
        "0.0 & 0.0", "0.0 & 0.0"
    ]
    expected_joined_table = "0.0 & 0.0 \\\\ \n0.0 & 0.0\\\\ \n"
    joined_table = E.joined_rows(current_table)
    assert joined_table.replace(" ", "") == expected_joined_table.replace(" ", "")

def test_multirow(): 
    headers = ["header1", "header2"]
    fill_data = np.zeros((2,2))

    multirow_table = E.mutlirow_subtable(headers, fill_data)

    assert len(multirow_table) == 2
    assert len(multirow_table[0].split("&")) == 4

def test_multicol(): 
    super_columns = ["na", 'na']
    columns = ["na", 'na', 'na', 'na']
    title = "na"
    rows_names = ["na", 'na']
    data_fill = np.zeros((2,2))

    table = E.multicol_subtable(super_columns, columns, title, rows_names, data_fill)
    
    assert len(table) == len(data_fill)+2
    assert len(table[0].split("&")) == len(super_columns)+1
    assert len(table[1].split("&")) == len(columns)

    assert len(table[3].split("&")) == data_fill.shape[0]+2

# TODO error check for incorrect input