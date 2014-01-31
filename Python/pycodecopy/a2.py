def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1

def is_valid_sequence(dna):

    """

    (str) -> bool

    Return True if and only if DNA sequence dna contains
    only instances of 'A', 'C', 'T', or 'G'.

    >>> is_valid_sequence('CTGA')
    True
    >>> is_valid_sequence('Bumblebutt')
    False
    >>> is_valid_sequence('1234')
    False
    >>> is_valid_sequence('AC12')
    False
    
    """

    is_dna = True
    for char in dna:
        if char not in 'ACTG':
            is_dna = False

    return is_dna

def insert_sequence(dna1, dna2, placey):
    """

    (str, str, int) -> str

    Inserts the string dna2 into the string dna1
    at index placey.
    
    >>> insert_sequence('ACTG', 'AC', 0)
    'ACACTG'
    >>> insert_sequence('ACTG', 'AC', 2)
    'ACACTG'
    >>> insert_sequence('ACTG', 'AC', 3)
    'ACTACG'
    >>> insert_sequence('ACTG', 'AC', -1)
    'ACTACG'
    >>> insert_sequence('ACTG', 'AC', 5)
    'ACTACG'
    >>> insert_sequence('ACTG', 'AC', 6)
    'ACTACG'
    """

    return dna1[:placey] + dna2 + dna1[placey:]

def get_complement(nucleotide):

    """

    (str) -> str
    
    Return the complement of str nucleotide (replace
    'A' with its complement 'T', 'G' with 'C',
    'T' with 'A', and 'C' with 'G'.

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    >>> get_complement('C')
    'G'
    >>> get_complement('')
    ''
    
    """

    if nucleotide == "A":
        return "T"
    elif nucleotide == "T":
        return "A"
    elif nucleotide == "G":
        return "C"
    elif nucleotide == "C":
        return "G"
    else:
        return nucleotide

def get_complementary_sequence(dna):

    """

    (str) -> str
    
    Return the complement of string dna (replace
    'A' with its complement 'T', 'G' with 'C',
    'T' with 'A', and 'C' with 'G' for ALL INSTANCES
    of these nucleotides).

    >>> get_complementary_sequence('AGTC')
    'TCAG'
    >>> get_complementary_sequence('AAAA')
    'TTTT'
    >>> get_complementary_sequence('')
    ''
    
    """

    if dna != '':
        dna = get_complement(dna[0]) + dna[0+1:]
    for i in range(1, len(dna)):
        dna = dna[:i] + get_complement(dna[i]) + dna[i+1:]
    return dna
