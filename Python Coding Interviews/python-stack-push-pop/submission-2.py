from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    copy_list = arr.copy()
    result = []
    while len(copy_list) > 0:
        result.append(copy_list.pop())
    return result


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
