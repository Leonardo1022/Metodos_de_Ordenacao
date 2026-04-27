from Sorting.util import file_to_list
"""
Complexidade: {
Pior: O(n log_2 n)
Médio: O(n log_2 n)
Melhor: O(n log_2 n)
} Obs: A complexidade não muda pois sempre será necessário fazer a divisão e a junção das listas

Esse tipo de ordenação funciona ao dividir continuamente uma lista em duas partes até chegar a
    uma lista de n = 1, após isso, é verificado os valores das duas partes para identificar a 
    menor e então encaixar na posição correta na instância anterior
"""
def merge_sort(random_list: list = file_to_list()) -> list:
    if len(random_list) > 1:
        middle = len(random_list) // 2
        left_list = random_list[:middle]
        right_list = random_list[middle:]

        merge_sort(left_list) # Parte esquerda
        merge_sort(right_list) # Parte direita

        i = 0 # Index da lista da esquerda
        j = 0 # Index da lista da direita
        k = 0 # Index da sub lista

        while i < len(left_list) and j < len(right_list):

            if left_list[i] < right_list[j]:
                random_list[k] = left_list[i]
                i += 1
            else:
                random_list[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):

            random_list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            random_list[k]= right_list[j]
            j += 1
            k += 1

    return random_list
