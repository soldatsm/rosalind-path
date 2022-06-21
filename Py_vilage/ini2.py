"""
Problem

Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

"""

path = r'C:\Users\Aster\Downloads\rosalind_ini2.txt'

with open(path, 'r') as read_file:
    a,b  = read_file.read().split(' ')
    read_file.close()

def hypotenuse(a,b):
    a = int(a)
    b = int(b)
    return int((a**2 + b**2))



if __name__ == '__main__':
    with open('ini2_answ.txt', 'w')  as write_file:
        write_file.write(str(hypotenuse(a, b)))
        write_file.close()
