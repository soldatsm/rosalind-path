"""
Problem
Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
"""

path = r'C:\Users\Aster\Downloads\rosalind_ini5(1).txt'
with open(path, 'r') as read_file:
    data = read_file.readlines()
    read_file.close()

answer_list = []   
for num, line in enumerate(data, 1): #enumerate allows to add iterabeble indexes 
    if num % 2 == 0:
        answer_list.append(line)

with open('ini5_answer.txt', 'a') as write_file:
    write_file.write(''.join(answer_list))
