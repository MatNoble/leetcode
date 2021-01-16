#==================================================
#==>      Title:                                     
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 
#==================================================

##################
#   Accumulate sum
##################
def accSum(n):
    if n == 1: return 1
    return accSum(n-1) + n

n = 10
print(f'1 + ... + {n} = {accSum(n)}')

##################
#        Factorial
##################
def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n

n = 3
print(f'{n}! = {factorial(n)}')

#####################
#  Fibonacci sequence
#####################
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

n = 5
print('1, 1, 2, 3, 5, 8, 13 ....')
print(f'第 {n} 位斐波那契数是 {fib(n)}')

