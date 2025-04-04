# lst = [0, 1, 7, 2, 4, 8] # -> 88
# lst = [1, 3, 5] # -> 30
# lst = [6] # -> 6
lst = [0] # -> 0


result = sum(lst[::2]) * lst[-1] if lst else 0
print(result)
