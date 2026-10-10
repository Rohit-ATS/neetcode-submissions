def add_two_numbers() -> int:
    user_input = input()
    user_input_list = list(map(int, user_input.split(",")))
    total_sum = sum(user_input_list)
    return total_sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
