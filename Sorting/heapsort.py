def heapify(arr,n,i):
    largest = i
    lchild = 2*i+1
    rchild = 2*i+2
    if (lchild<n and arr[lchild]>arr[largest]):
        largest  = lchild
    if (rchild<n and arr[rchild]>arr[largest]):
        largest = rchild
    if largest!=i:
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,n,largest)


def heapSort(arr,n):
    #First restructure the given array into max-heap
    #parent of last node in array is n-1//2
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)
    return arr

if __name__=='__main__':
    arr = [3,4,5,6,1,2,3,8,9,0]
    print(heapSort(arr,len(arr)))
