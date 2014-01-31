def count_adjacent_repeats(s):
    '''
    (str) -> int

    Returns the number of times that two adjacent characters
    are identical in a string s.

    >>>count_adjacent_repeats('abccdeffggh')
    3

    '''

    repeats = 0

    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            repeats += 1

    return repeats

def shift_left(L):
    """
    (list) -> NoneType

    Shift each item in L one position to the left
    and shift the first item to the last position.

    Precondition: len(L) >= 1
    """

    first_item = L[0]
    for i in range(len(L)-1):
        L[i] = L[i+1]
    L[-1] = first_item

    print(L)
