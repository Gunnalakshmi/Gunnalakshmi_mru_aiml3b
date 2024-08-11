#Write a function to generate the first n Fibonacci numbers using a loop. For example, if n = 6, the output should be [0, 1, 1, 2, 3, 5].
def fib(n):
    if n <= 1:
        return n
    return fib(n-2)+fib(n-1)
def get_fib(n,a):
    for i in range(n):
        a.append(fib(i))
    return a
a  = []
n = int(input())
print(get_fib(n,a))
