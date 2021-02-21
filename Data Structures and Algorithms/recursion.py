#==================================================
#==>      Title: recursion                                    
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==================================================

# #################
#   Accumulate sum
# #################
def accSum(n):
    if n == 1: return 1
    return accSum(n-1) + n

n = 10
print(f'1 + ... + {n} = {accSum(n)}')

# #################
#        Factorial
# #################
def factorial(n):
    if n == 1: return 1
    return factorial(n-1) * n

n = 3
print(f'{n}! = {factorial(n)}\n')

# ####################
#  Fibonacci sequence
# ####################
def fibDP(n):  ## downUp
    if n < 1: return 0
    if n <= 2: return 1
    dp = [0]*(n+1)
    dp[1] = dp[2] = 1
    i = 3
    while i <= n:
        dp[i] = dp[i-1] + dp[i-2]
        i += 1
    return dp[n]

n = 10
print('1, 1, 2, 3, 5, 8, 13 ....')
print(f'第 {n} 位斐波那契数是 {fibDP(n)}')

def fib(n):
    if n < 1: return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
n = 10
print('1, 1, 2, 3, 5, 8, 13 ....')
print(f'第 {n} 位斐波那契数是 {fib(n)}')

def fibRecursion(n):  ## upDown
    def upDown(n):
        if n < 1: return 0
        if n <= 2:
            return 1
        if dp[n]: return dp[n]
        dp[n] = upDown(n-1) + upDown(n-2)
        return dp[n]
    dp = [0] * (n+1)
    return upDown(n)
n = 10
print('1, 1, 2, 3, 5, 8, 13 ....')
print(f'第 {n} 位斐波那契数是 {fibRecursion(n)}\n')


# ####################
#     reverse String
# ####################
def reverseString(s):
    if not s: return ''
    return reverseString(s[1:]) + s[0]

s = 'matnoble'
reverseString(s)
