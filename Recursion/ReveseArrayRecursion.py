def reverse(arr,start,stop):
    if start<stop-1:
        arr[start],arr[stop-1] = arr[stop-1],arr[start]
        reverse(arr,start+1,stop-1)

    # print(arr)

if __name__=='__main__':
    arr = [1,2,3,4,5]
    reverse(arr,0,len(arr))
    print(arr)
