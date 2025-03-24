lst = [1, 2, 3, 4, 5, 6]  # [[1, 2, 3], [4, 5, 6]]
# lst = [1, 2, 3]           # [[1, 2], [3]]
# lst = [1, 2, 3, 4, 5]     # [[1, 2, 3], [4, 5]]
# lst = [1]                 # [[1], []]
# lst = []                  # [[], []]


if not lst: 
    lst = [[], []]
else:
    half = (len(lst) + 1) // 2
    lst = [lst[:half], lst[half:]]


print("Expected [[1, 2, 3], [4, 5, 6]] => ", lst)
