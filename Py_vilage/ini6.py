"""
Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, 
where words are separated by spaces. Words are case-sensitive, 
and the lines in the output can be in any order.
"""


#from collections import Container

path = r'C:\Users\Aster\Downloads\rosalind_ini6.txt'
with open(path, 'r') as read_file:
    data = read_file.readline().strip('\n').split(' ') # cause we need words not full string strip
                                                       #strip need since last word contains \n and, for python,
                                                       #it looks like other word
    read_file.close()

def dictioner(string):
    diction = {}
    for word in string:
        if word  in diction:
            diction[word] += 1
        else:
            diction[word] = 1
    return diction

answer = dictioner(data)
with open('ini6_answer.txt', 'a') as write_file:
    for key, value in answer.items():
        write_file.write(f'{key} {value} \n')