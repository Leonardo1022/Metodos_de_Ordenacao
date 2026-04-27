import random

def create_list():
    random_list = [random.randint(1, 99) for _ in range(1000000)]
    with open("1M random_list.txt", "w") as file:
        file.write(str(random_list))