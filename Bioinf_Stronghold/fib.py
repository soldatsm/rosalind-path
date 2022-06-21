
"""
Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, 
if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

"""

data = r'C:\Users\Aster\Downloads\rosalind_fib (1).txt'

with open(data, 'r') as read_file:
    n, k = read_file.readline().split(' ')
    read_file.close()


def fibonacci(n,k):
    f1,f2 = 0,1

    for _ in range(int(n)):
        f1,f2 = f2, f2 + f1*int(k)

    return f1

with open('fib_answer.txt', 'w') as write_file:
    write_file.write(str(fibonacci(n, k)))
    write_file.close()
