def linear_Sum(arr,n):
    if n==0:
        return 0
    else:
        return linear_Sum(arr,n-1)+arr[n-1]


def binary_sum(arr,start,stop):
    if start>=stop:
        return 0
    elif start==stop-1:
        return arr[start]
    else:
        mid = (start+stop)//2
        return binary_sum(arr,start,mid)+binary_sum(arr,mid,stop)
if __name__=='__main__':
    arr = [1,2,3,4,5]
    print(linear_Sum(arr,len(arr)))
    print(binary_sum(arr,0,len(arr)))
