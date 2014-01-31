def convert_to_celsius(fahrenheit):
    '''(number) -> float

    Return the number of Celsius degrees equivalent to Fahrenheit degrees
    >>> convert_to_celsius(32)
    0
    >>> convert_to_celsius(212)
    100
    '''
    return (fahrenheit - 32) * 5 /9

def convert_to_fahrenheit(celsius):
    '''(number) -> float

    Return the number of Fahrenheit degrees equivalent to Celsius degrees
    >>> convert_to_fahrenheit(0)
    32
    >>> convert_to_fahrenheit(100)
    212
    '''
    return celsius*9/5 + 32
