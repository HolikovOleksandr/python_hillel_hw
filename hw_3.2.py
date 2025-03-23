lst_a = [12, 3, 4, 10]     # [10, 12, 3, 4]
lst_b = [1]                # [1]
lst_c = []                 # []
lst_d = [12, 3, 4, 10, 8]  # [8, 12, 3, 4, 10]


def set_last_list_item_to_first(lst):
    if len(lst) > 1:
        lst.insert(0, lst.pop())

    return lst


print("Expected [10, 12, 3, 4] => ", set_last_list_item_to_first(lst_a))
print("Expected [1] => ", set_last_list_item_to_first(lst_b))
print("Expected [] => ", set_last_list_item_to_first(lst_c))
print("Expected [8, 12, 3, 4, 10] => ", set_last_list_item_to_first(lst_d))