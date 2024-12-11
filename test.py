import requests
from bs4 import BeautifulSoup
import pandas as pd

def print_char(coordinates_char):
    max_x = max(x[0] for x in coordinates_char)  
    max_y = max(x[1] for x in coordinates_char)  
    #print(max_x,max_y)
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, ch in coordinates_char:
        if 0 <= x <= max_x and 0 <= y <= max_y:
            grid[y][x] = ch

    for row in grid:
        print(''.join(row))

def swap_indices_in_tuples(tuple_list, index1, index2):
    swapped_list = [
        tuple(tpl[index2] if i == index1 else tpl[index1] if i == index2 else val for i, val in enumerate(tpl))
        for tpl in tuple_list
    ]
    return swapped_list

def convert_first_two_to_int(tuple_list):
    converted_list = [(int(tpl[0]), int(tpl[1]) if len(tpl) > 1 else tpl[1], *tpl[2:]) for tpl in tuple_list]
    return converted_list

def print_file(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the document: {response.status_code}")
    soup = BeautifulSoup(response.text, 'html.parser')

    tables = soup.find_all('table')
    dataframes = []  # To store extracted tables as DataFrames

    for table in tables:
        rows = table.find_all('tr')
        table_data = []
        for row in rows:
            cells = row.find_all(['td'])
            table_data.append([cell.text.strip() for cell in cells])
        df = pd.DataFrame(table_data)
        dataframes.append(df)
    if dataframes:
        list_of_tuples = [tuple(row) for row in dataframes[0].to_numpy()]
        list_of_tuples.pop(0)
        new_list_of_tuples = convert_first_two_to_int(swap_indices_in_tuples(list_of_tuples,1,2))
        #print(new_list_of_tuples)
        print_char(new_list_of_tuples)
    else:
        print("No tables found in the document.")

#Execute the funtion
print_file("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")