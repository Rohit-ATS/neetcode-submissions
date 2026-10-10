from typing import List

def read_integers() -> List[int]:
    user_input = input()
    num_list = list(map(int, user_input.split(",")))
    return num_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
