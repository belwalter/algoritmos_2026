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

print(fibonacci(150))
# print(fibonacci_r(50))