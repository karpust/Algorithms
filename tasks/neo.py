import math
import os
import random
import re
import sys


lst = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']


def decode_matrix(some_input):
    some_input = some_input.rstrip().split('\n')
    numbers = some_input.pop(0).split()
    n = int(numbers[0])  # row
    m = int(numbers[1])  # column
    matrix = [i[j] for j in range(m) for i in some_input]
    alnum_count = 0
    notalnum = []
    for i in range(len(matrix)-1):
        if matrix[i].isalnum():
            alnum_count += 1
            if notalnum and i > notalnum[len(notalnum) - 1]:
                for i in notalnum:
                    matrix[i] = '*'
                notalnum = []
        else:
            if alnum_count > 0:
                notalnum.append(i)
    matrix = ''.join(matrix)
    matrix = re.sub(r'\*+', ' ', matrix)
    return matrix


c = 1 if 'This is Matrix#  %!' == 'This is Matrix#  %!' else 2
print(c)





s = """7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!"""
# s = input()
print(decode_matrix(lst))


def test_decode_matrix():
    answer = decode_matrix("""7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!""")
    assert answer == 'This is Matrix#  %!', f'wrong answer: {answer}'

    answer = decode_matrix("""4 6
T%Mic&
h%axr%
iit#p!
ssrst&""")
    assert answer == 'This isMatrix scrpt&%!&', f'wrong answer: {answer}'

    # answer = decode_matrix("""""")
    # assert answer == 'This is Matrix#  %!', f'wrong answer: {answer}'
    #
    # answer = decode_matrix("""""")
    # assert answer == 'This is Matrix#  %!', f'wrong answer: {answer}'
    #
    # answer = decode_matrix("""""")
    # assert answer == 'This is Matrix#  %!', f'wrong answer: {answer}'
    #
    # answer = decode_matrix("""""")
    # assert answer == 'This is Matrix#  %!', f'wrong answer: {answer}'


test_decode_matrix()



"""
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
if n > 0 and m < 100:
    matrix = [i[j] for j in range(m) for i in matrix]
    alnum_count = 0
    notalnum = []
    for i in range(len(matrix)-1):
        if matrix[i].isalnum():
            alnum_count += 1
            if notalnum and i > notalnum[len(notalnum) - 1]:
                for i in notalnum:
                    matrix[i] = '*'
                notalnum = []
        else:
            if alnum_count > 0:
                notalnum.append(i)
    matrix = ''.join(matrix)
    matrix = re.sub(r'\*+', " ", matrix)
print(matrix)
"""

