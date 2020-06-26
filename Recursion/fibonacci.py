import timeit
def bad_fib(n):
    if n<=1:
        return n
    else:
        return bad_fib(n-1)+bad_fib(n-2)

def good_fib(n):
    if n<=1:
        return (n,0)
    else:
        a,b = good_fib(n-1)
        return (a+b,a)

if __name__=='__main__':
    print(timeit.timeit("bad_fib(10)",setup='from __main__ import bad_fib'))
    print(timeit.timeit("good_fib(10)",setup='from __main__ import good_fib'))
