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