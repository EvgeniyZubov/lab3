import numpy as np
import random

def proc21():
    A = float(input("Введіть А: "))
    B = float(input("Введіть B: "))
    N1 = int(input("Введіть N1: "))
    N2 = int(input("Введіть N2: "))
    N3 = int(input("Введіть N3: "))
    if A == 0 or B == 0:
        print("Error: A and B must be non-zero numbers.")
        return

    print("Завдання№1 = ",Calc(A,B,N1))
    print("Завдання№2 = ", Calc(A, B, N2))
    print("Завдання№3 = ", Calc(A, B, N3))




def Calc(A,B,Op):
    if Op == 1:
        return A-B
    elif Op == 2:
        return A*B
    elif Op == 3:
        return A/B
    else:
        return A+B


def matrix14():
    filename = ("input.txt")
    with open(filename) as f:
        mean(f)
        f.seek(0)
        rand(f)


def mean(f):
    rule = f.readline().split(" ")
    M = int(rule[0])
    N = int(rule[1])

    count = 0
    ariph = 0
    bigger_one = 0
    bigger_list = []
    big_list = []
    ariph_list = []

    arr = np.loadtxt(f, max_rows=M)
    print(arr)
    for i in range (0,M):
        for j in range (0,N):
            ariph += arr[i][j]


        ariph /= N
        ariph_list.append(ariph.item())
        ariph = 0
        for j in range (0,N):
            if arr[i][j] > ariph_list[i]:
                bigger_one = arr[i][j]
                bigger_list.append(bigger_one.item())
                bigger_one = 0
                count += 1

        print("array№",[i]," = ",bigger_list, "\n Кількість чисел більших за с.а. ряду: ", count)
        count = 0
        bigger_list = []


    print("Mean of ariph:", ariph_list)



def rand(f):
    rule = f.readline().split(" ")
    M = int(rule[0])
    N = int(rule[1])

    arr = np.loadtxt(f, max_rows=M)

    default = np.zeros((M,N))

    for i in range(M):
        for j in range(N):
            default[i][j] = random.randint(0, 20)

    print("Дефолт рандом = \n", default)


    for i in range(M):
        for j in range(N):
            default[i][j] *= arr[i][j]


    print("Дефолт рандом * Массив = \n", default)
    print("Массив: \n", arr)
