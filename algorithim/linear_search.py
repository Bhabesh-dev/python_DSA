def linear_search(input_list, target):
    """
    :param input_list:
    :param target:
    :return: the index position of the target if found
    """
    for item in range(0, len(input_list)):
        if input_list == target:
            return item
    return None


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 12)
result1 = linear_search(numbers, 10)

verify(result)
verify(result1)
