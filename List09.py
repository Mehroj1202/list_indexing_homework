def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i=0
    while i<len(list1):
        if list1[i]==list1[-1]:
            return True
        else:
            return False
        i+=1
print(main([0, 0, 0, 0, 0]))
print(main(['x', 'x', 'y', 'y', 'z']))