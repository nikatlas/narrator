from typing import Any, List


def flatten(nested_list: List[Any]) -> List[Any]:
    flat_list = []
    stack = [nested_list]

    while stack:
        current = stack.pop()
        for item in current:
            if isinstance(item, list):
                stack.append(item)
            else:
                flat_list.append(item)

    return flat_list
