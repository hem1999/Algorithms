def binarySearch(array,lookup,low,high):
    if low>high:
        return "Not Found"
    print("Current Search Area: ",array[low:high+1])
    mid = (low+high)//2
    if array[mid]==lookup:
        return f"lookup found at {mid}"
    elif array[mid]>lookup:
        return binarySearch(array,lookup,low,mid-1)
    else:
        return binarySearch(array,lookup,mid+1,high)



if __name__=='__main__':
    array = [0,102,109,111,1000,1111,1444,1999]
    print(binarySearch(array,1444,0,len(array)-1))
