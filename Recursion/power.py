from timeit import timeit
def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
#O(n)


def Epower(x,n):
    if n==0:
        return 1
    else:
        partial = Epower(x,n//2)
        result = partial*partial
        if n%2==1:
            result = result*x
        return result
    #O(logn)

if __name__=='__main__':
    print(power(2,100))
    print(Epower(2,100))
    print(timeit('power(2,100)',setup = 'from __main__ import power'))
    print(timeit('Epower(2,100)',setup = 'from __main__ import Epower'))
