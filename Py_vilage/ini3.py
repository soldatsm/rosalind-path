""""
Problem
Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d (with space in between), 

inclusively. In other words, we should include elements s[b] and s[d] in our slice.

"""


path = r'C:\Users\Aster\Downloads\rosalind_ini3 (1).txt'

with open(path, 'r') as read_file:
    string = read_file.readline().strip()
    a,b,c,d = read_file.readline().split(' ')
    read_file.close()

answer = string[int(a):int(b)+1] + ' ' + string[int(c):int(d)+1]

with open('answer_ini3.txt', 'w') as write_file:
    write_file.write(answer)
    write_file.close()