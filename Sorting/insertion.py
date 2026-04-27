from Sorting.util import file_to_list

"""
Complexidade: {
Pior: O(n^2)
Médio: O(n^2)
Melhor: O(n)
}

A ordenação por inserção funciona ao comparar um elemento e colocá-lo na posição correta se comparado
    ao seu vizinho anterior e posterior
"""
def insertion_sort(random_list: list = file_to_list()) -> list:
    n = len(random_list) - 1
    i = 0
    while i < n:
        j = i + 1
        print(j)
        if random_list[i] > random_list[j]:
            compare_number = random_list[j] # Número a ser comparado com os anteriores
            k = i
            while random_list[k] > compare_number and k >= 0:
                random_list[k + 1] = random_list[k]
                k -= 1
            if k == -1: # Caso o primeiro item seja maior que o número comparado
                random_list[0] = compare_number
            else:
                random_list[k + 1] = compare_number
        i += 1
    return random_list