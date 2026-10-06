from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    new_dict = {}
    for key in list(my_dict.keys()):
        if key in keys:
            del my_dict[key]
    return my_dict




# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))
