# FACTORIAL !
# factorial(5)  = 5 * 4 * 3 * 2 * 1
# 5!

# fac(5) = 5 * fac(4)
# fac(4) = 4 * fac(3)
# fac(3) = 3 * fac(2)
# fac(N) = N * fac(N-1) -> fac(0) = 1

def factorial_r(num: int) -> int:
    if num == 0:
        return 1
    else:
        return num * factorial_r(num-1)

def factorial(num: int) -> int:
    result = 1
    for i in range(1, num + 1):
        result = result * i

    return result

# print(factorial(5))
# print(factorial_r(5))

# fib(N) = fib(N-1) + fib(N-2) -> fib 0=0, fib 1=1 

# fibonacci 
def fibonacci_r(num: int) -> int:
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci_r(num-1) + fibonacci_r(num-2)

def fibonacci(num):
    fib_1 = 0
    fib_2 = 1
    for i in range(2, num+1):
        fib_aux = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_aux
    
    return fib_aux

# print(fibonacci(150))
# print(fibonacci_r(50))


#  5 + 4 + 3 + 2 + 1 + 0 = 15
# sum(n) = n + sum(n-1)          ->   sum(0) = 0

def suma(num: int) -> int:
    if num == 0:
        return num
    else:
        return num + suma(num-1)
    
# print(suma(5))



# 2 * 3 = 2 + 2 + 2 = 6
# prod(n, m) = n + prod(n, m-1)    -> n, m = 0 -> 0


def prod(n: int, m: int) -> int:
    if m==0:
        return 0
    else:
        return n + prod(n, m-1)

# print(prod(0, 3))

# h(n) = 1/n + 1/n-1 + 1/n-2 .... n = 1 -> 1

def serie_h(num: int) -> float:
    if num == 1:
        return num
    else:
        return 1/num + serie_h(num-1)

# print(serie_h(4))


# 523 -> 52     5       -> n < 10 = 1
        # +1      +1

def count(num: int) -> int:
    if num <= 10:
        return 1
    else:
        return 1 + count(num // 10)

# print(count(5))
# print(count(52))
# print(count(523))
# print(count(5023))


# invertir(hola) = a + invertir(hol) -> cadena = ''


def invertir(cadena: str) -> str:
    if cadena == '':
        return cadena
    else:
        return cadena[-1] + invertir(cadena[:-1])


print(invertir('hola'))
