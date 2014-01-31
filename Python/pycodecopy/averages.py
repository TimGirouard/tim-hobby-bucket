def averages(grades):
    '''

    (list of lists of numbers) -> list of floats

    Return a new list in which each item is the average
    of the grades in the inner list at the corresponding
    position of grades.

    >>>averages([[70,75,80], [70,80,90,100], [80,100]])
    [75.0, 85.0, 90.0]

    '''

    averages = []
    
    for course in grades:
        #Calculate the average of course and
        #append it to averages.
        
        total = 0
        
        for mark in course:
            total += mark

        averages.append(total/len(course))

    return averages
