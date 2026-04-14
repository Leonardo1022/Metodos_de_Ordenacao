from Sorting.util import file_to_list

def selection_sort(random_list: list = file_to_list()):
    n = len(random_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if random_list[j] < random_list[min_index]:
                min_index = j

        random_list[i], random_list[min_index] = random_list[min_index], random_list[i]

    #print(random_list)
    return random_list