def calculate_average(asn_grades):
    '''
    list of lists of [str, number]) -> float

    Return the average of the grades in asn_grades.

    >>> calculate_average([['A1', 80], ['A1', 90]])
    85.0
    '''

    sum_grades = 0

    for i in range(len(asn_grades)):
        sum_grades += asn_grades[i][1]

    return sum_grades/len(asn_grades)
