n = int(input("n value to find nth fibonaaci number"))
memoization = [-1 for i in range(n+1)]

def topDownFB(n):
    if memoization[n]==-1:
        if n==0 or n==1:
            return n
        res = topDownFB(n-1)+topDownFB(n-2)
        memoization[n]=res
    return memoization[n]

def bottomUpFB(n):
    fib = [0 for i in range(n+1)]
    fib[0]=0
    fib[1]=1
    for i in range(2,n+1):
        fib[i]=fib[i-1]+fib[i-2]
    return fib[n]

print(f"top down: {topDownFB(n)}")
print(f"Bottom Up: {bottomUpFB(n)}")
