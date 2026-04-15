import random

def create_list():
    random_list = [random.randint(1, 99) for _ in range(1000)]
    with open("data.txt", "w") as file:
        file.write(str(random_list))