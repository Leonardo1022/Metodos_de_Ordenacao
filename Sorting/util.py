import ast

default_file = r"/Sorting/1M random_list.txt"

def file_to_list(data_file: str = default_file) -> list:
    with open(data_file, "r") as file:
        file_str = file.read()
        random_list = ast.literal_eval(file_str) # 1000 elementos de 1 a 99
        return random_list