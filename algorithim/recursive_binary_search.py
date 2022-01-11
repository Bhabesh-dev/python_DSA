def recursive_binary_search(input_list, target):
    """
    recursive method
    tail call optimization - read on this
    :param input_list:
    :param target:
    :return:
    """
    if len(input_list) == 0:
        return False
    else:
        midpoint = len(input_list)//2

        if(input_list[midpoint]) == target:
            return True
        else:
            if input_list[midpoint] < target:
                return recursive_binary_search(input_list[midpoint+1:])
            else:
                return recursive_binary_search(input_list[:midpoint])


def verify(res):
    print(f"Target found : {res} ")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = recursive_binary_search(numbers, 12)
verify(result)
result = recursive_binary_search(numbers, 10)
verify(result)
