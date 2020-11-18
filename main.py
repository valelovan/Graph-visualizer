import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Creates nxm sized grid
def grid(n, m):

    yaxis = '{num:>2}{line:1}'

    for i in range(n - 1):
        print(yaxis.format(num = str(n - 1 - i), line = '|'))
    print('  |', end='')

    for i in range(m - 1):
        print('-', end='')
    print()


yaxis = '{num:>2}{line:1}'

#def plot_graph(x, y, numbers):
#    for i in range(x):
#        if i in numbers:
            







grid(100,200)

points = {}



for i in range(25):
    num = i ** 2
    points[i] = num

print(points)