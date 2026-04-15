# Fazer os métodos das ordenações e procurar valores específicos utilizando a pesquisa binária
import timeit
import cProfile
import pstats
import Sorting
from binary_search import binary_search

opt = 2
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
        index = binary_search(20, ordered_list, 0, len(ordered_list))
        print(f"Número procurado: {ordered_list[index]} no index[{index}]")