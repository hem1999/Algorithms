def dec2bin(n):
    if n==0:
        return 0
    dec2bin(n//2)
    print(n%2,end="")

if __name__=='__main__':
    dec2bin(8)
    print()
    dec2bin(16)
    print()
    dec2bin(32)
