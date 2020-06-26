def factorial(n):
    print(f"Calling factorial({n})")
    if n==0:
        print(f"Current Function return 1")
        return 1
    else:
        print(f"current function returns {n}*factorial({n-1})")
        return n*factorial(n-1)

if __name__=='__main__':
    print(factorial(5))
