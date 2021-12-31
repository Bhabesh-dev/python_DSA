def binary_search(input_list, target):
    """
    iterative  method
    :param input_list:
    :param target:
    :return: return the index of the value from the list if found
    """
    first = 0
    last = len(input_list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if input_list[midpoint] == target:
            return midpoint
        elif input_list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None



