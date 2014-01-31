def count_vowels(s):
    '''
    (str) -> int

    Count the number of vowels in s. Do not treat 'y'
    as a vowel.
    
    >>> count_vowels('Happy Anniversary!')
    5
    >>> count_vowels('xyz')
    0
    '''

    vowels = 0
    for char in s:
        if char in 'aeiou' or char in 'AEIOU':
            vowels += 1
    return vowels

def collect_vowels(s):
    '''
    (str) -> str

    Count the number of vowels in s. Do not treat 'y'
    as a vowel.
    
    >>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>> count_vowels('xyz')
    ''
    '''

    vowelstring = ''
    for char in s:
        if char in 'aeiou' or char in 'AEIOU':
            vowelstring = vowelstring + char
    return vowelstring
