def sum_items(list1,list2):
    """
    (list of numbers, list of numbers) -> list of numbers

    Return a new list in which each item is the sum of the
    corresponding position for list1 and list2.

    Precondition: len(list1)==len(list2)

    >>sum_items([1,2,3], [2,4,2])
    [3,6,5]
    """

    sum_list = []

    for i in range(len(list1)):
        sum_list.append(list1[i]+list2[i])

    return sum_list

def count_matches(s1, s2):
    """
    (str, str) -> int
    Return the number of positions in s1 that contain the
    same character at the corresponding position of s2.

    Precondition: len(s1) == len(s2)

    >>> count_matches('ate','ape')
    2
    >>> count_matches('head', 'hard')
    2
    """

    num_matches = 0

    for i in range(len(s2)):
        if s1[i] == s2[i]:
            num_matches += 1

    return num_matches
