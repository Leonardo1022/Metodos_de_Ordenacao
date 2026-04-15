"""
Procura o número alvo numa lista por meio do método de busca binária com recursão e retorna a posição dele nela
Recebe o número 'target', a lista em 'search_list', o valor mínimo de busca 'low' e o valor máximo 'high'
Retorna o index do número alvo na lista
"""
def binary_search(target: int, search_list: list, low: int, high: int) -> int:
    n = low + ((high - low) // 2)

    if search_list[n] == target:
        return n
    elif search_list[n] > target and n != 0: # Caso esteja na primeira metade
        return binary_search(target, search_list, low, n)
    elif search_list[n] < target and n != (high - 1): # caso esteja na segunda metade
        return binary_search(target, search_list, n, high)
    else: # Caso o número não esteja presente na lista
        return -1