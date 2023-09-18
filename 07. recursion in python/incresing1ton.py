def oneton(n):
    # base case
    if(n < 1):
        return
    else:
        oneton(n-1)
        print(n)

oneton(5)