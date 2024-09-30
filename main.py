# u1
import math


def fun1():
    for i in range(1, 11):
        print(i)
fun1()

# u2a

def fun2(n):
    for i in range(1, 1 + n):
        print(i)
fun2(15)

# u2b

def fun2b(n):
    for i in range(1, 1 + n):
        if i < n:
            print(i, end=',')
        else:
            print(i)
fun2b(15)

# u3

def fun3(n):
    for i in range(5, n + 1, 2):
        print(i)
fun3(15)

#u4
def fun4(n):
    for i in range(n, n + 1):
        print(i, i**2)
fun4(9)

#u5
import math
def fun5(odkial, pokial):
    for i in range(odkial, pokial + 1):
        math.sqrt(i)
        zaokr_f = round(math.sqrt(i), 2)
        print (i,zaokr_f)
fun5(1,5)

#u6
def fun6 (n):
    for x in range(1, 21):
        if x==3:
            print("x=3 funkcia nie je definovatelna")
        else:
            vzorec_y = (x ** 2 - 1) / (x - 3)
            print ("x = y =",vzorec_y )

fun6(20)

#u7
def fun7(n):
    for i in range(1, n+1):
        if i%3 == 0:
            print(i)
fun7(10)

#u8
def fun8(n):
    for i in range(1, n +1):
        if i%2 == 0:
            print(i)
fun8(20)

#u9
def fun9(z, k):
    for i in range(z, k+1):
        if i%2 !=0:
            print(i)
fun9(6, 10)

#u10
def fun10(n):
    for i in range(n, 0, -1):
        print(i, end=' ')

fun10(5)

#u11
def fun11(n):
    for i in range(0, n+1):
        if i%7 ==0 and i%4==0:
            print(i)
fun11(100)

#u12
def fun12(n):
    spolu = sum(range(1, n+1))
    print(spolu)
fun12(100)

#u13
def fun13(n):
    spolu_parne = sum(i for i in range(1, n+1) if i%2 == 0)
    print(spolu_parne)
fun13(10)

#u14
def fun14(zaciatok, koniec):
    pocet = sum(1 for i in range(zaciatok, koniec+1) if i%8 == 0)
    print(pocet)
fun14(1,30)
