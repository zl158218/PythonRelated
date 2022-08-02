# -*-  coding:utf-8 -*-
import random
list_a = [random.randint(1, 50) for x in range(0, 10)]
print(list_a)


# def find_smaill_all(arr):
#     semlllest = arr[0]
#     semlllest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < semlllest:
#             semlllest = arr[i]
#             semlllest_index = i
#     return semlllest_index

# def selection_sort(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         semallet = find_smaill_all(arr)
#         new_arr.append(arr.pop(semallet))
#     return new_arr


# if __name__ == "__main__":
#     print(selection_sort(list_a))

















def selection_sort(arr):
    """
    选择排序
    """
    new_arr = []
    while arr:
        semill_val = arr[0]
        semill_ind = 0
        for i in range(1, len(arr)):
            if arr[i] < semill_val:
                semill_ind = i
                semill_val = arr[i]

        new_arr.append(arr.pop(semill_ind))
    print(new_arr)


selection_sort(list_a)