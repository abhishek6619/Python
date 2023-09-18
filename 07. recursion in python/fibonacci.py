def fibo(n):
    # base case
    if(n == 0 or n == 1):
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(6))
print(fibo(7))
print(fibo(8))
print(fibo(9))
print(fibo(10))