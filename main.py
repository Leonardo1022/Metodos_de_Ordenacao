# Fazer os métodos das ordenações e procurar valores específicos utilizando a pesquisa binária
import timeit
import cProfile
import pstats
import Sorting
from binary_search import binary_search

opt = 1
match opt:
    case 1:
        profiler = cProfile.Profile()
        profiler.enable()

        tempo_radix = timeit.timeit(
            lambda: Sorting.radix_sort(),
            number=100
        )

        tempo_selection = timeit.timeit(
            lambda: Sorting.selection_sort(),
            number=100
        )

        tempo_insertion = timeit.timeit(
            lambda: Sorting.insertion_sort(),
            number=100
        )

        profiler.disable()

        stats = pstats.Stats(profiler)
        stats.sort_stats("time").print_stats()

        print(f"Radix: {tempo_radix}\nSelection: {tempo_selection}\nInsertion: {tempo_insertion}")

    case 2:
        ordered_list = Sorting.radix_sort()
        target_list = [1, 3, 6, 8, 9, 10, 22, 59, 70, 89]

        for target in target_list:
            index = binary_search(target, ordered_list, 0, 1000)
            print(f"Número procurado: {ordered_list[index]} no index[{index}]")