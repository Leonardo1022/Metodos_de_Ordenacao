from Sorting.util import file_to_list

def insertion_sort(random_list: list = file_to_list()) -> list:
    n = len(random_list)
    for i in range(n - 1):
        j = i + 1
        if random_list[i] > random_list[j]:
            while random_list[i] > random_list[j] and i >= 0:
                random_list[i], random_list[j] = random_list[j], random_list[i]
                j = i
                i -= 1
    #print(random_list)
    return random_list