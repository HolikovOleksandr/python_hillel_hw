lst_a = [1, 2, 3, 4, 5, 6]  # [[1, 2, 3], [4, 5, 6]]
lst_b = [1, 2, 3]           # [[1, 2], [3]]
lst_c = [1, 2, 3, 4, 5]     # [[1, 2, 3], [4, 5]]
lst_d = [1]                 # [[1], []]
lst_e = []                  # [[], []]


def split_list_into_halves(lst):
    if not lst: return [[], []]
    half = (len(lst) + 1) // 2
    return [lst[:half], lst[half:]]


print("Expected [[1, 2, 3], [4, 5, 6]] => ", split_list_into_halves(lst_a))
print("Expected [[1, 2], [3]] => ", split_list_into_halves(lst_b))
print("Expected [[1, 2, 3], [4, 5]] => ", split_list_into_halves(lst_c))
print("Expected [[1], []] => ", split_list_into_halves(lst_d))
print("Expected [[], []] => ", split_list_into_halves(lst_e))
