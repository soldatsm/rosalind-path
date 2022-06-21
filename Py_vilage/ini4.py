"""
Problem
Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.

"""

path = r'C:\Users\Aster\Downloads\rosalind_ini4.txt'

with open(path, 'r') as read_file:
    a,b = read_file.readline().split(' ')
    read_file.close()

answer = sum([i for i in range(int(a), int(b)+1) if i % 2 != 0]) #list coprehension

with open('answer_ini4.txt', 'w') as write_file:
    write_file.write(str(answer))
    write_file.close()
        