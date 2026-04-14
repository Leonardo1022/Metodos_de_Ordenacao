import ast

def file_to_list(data_file: str = r"C:\Users\leona\PycharmProjects\Metodos_de_Ordenacao\Sorting\data.txt"):
    with open(data_file, "r") as file:
        file_str = file.read()
        random_list = ast.literal_eval(file_str) # 1000 elementos de 1 a 99
        return random_list