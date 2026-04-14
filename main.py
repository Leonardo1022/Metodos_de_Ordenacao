import timeit
import Sorting
import cProfile
import pstats

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