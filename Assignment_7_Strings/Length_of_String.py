#Program to calculate the lenghth of a string ,string is given by user

def length(string):
    '''
    Enter a string of your choice

    >>> length('silky')
    5

    >>> length('divesh')
    6

    >>> length('sareena')
    7
    '''

    print(len(string))

length('silky')
length('Divesh')
length('Sareena')

import doctest

doctest.testmod()