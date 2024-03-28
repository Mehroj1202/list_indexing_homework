def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    if list_num[0]>list_num[-1]:
        return list_num[0]
    elif list_num[0]<list_num[-1]:
        return list_num[-1]
    else:
        return "Equal"
print(main([12, 2, 5, 2, 7, 9, 1]))