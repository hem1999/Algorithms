class Sorting():
    def __init__(self,arr,asc = False):
        self.arr = arr
        self.asc = asc

    def bubble_sort(self):
        for j in range(len(self.arr)):
            for i in range(len(self.arr)-j-1):
                if self.asc:
                    if self.arr[i]>self.arr[i+1]:
                        self.arr[i],self.arr[i+1] = self.arr[i+1],self.arr[i]
                else:
                    if self.arr[i]<=self.arr[i+1]:
                        self.arr[i],self.arr[i+1] = self.arr[i+1],self.arr[i]
        return self.arr

    def merge_sort(self):
        def split(arr):
            if len(arr)<=1:
                return arr
            middle_index = len(arr)//2
            left = arr[:middle_index]
            right = arr[middle_index:]
            sleft = split(left)
            sright = split(right)
            return merge(sleft,sright)


        def merge(left,right):
            result = []
            while(left and right):
                if self.asc:
                    if left[0]<=right[0]:
                        result.append(left[0])
                        left.pop(0)
                    else:
                        result.append(right[0])
                        right.pop(0)
                else:
                    if left[0]>right[0]:
                        result.append(left[0])
                        left.pop(0)
                    else:
                        result.append(right[0])
                        right.pop(0)

            if left:
                result+=left
            if right:
                result+=right
            return result
        return split(self.arr)

    def quick_sort():
        

    def radix_sort():
        pass

    def insertion_sort():
        pass
if __name__=='__main__':
    #Let's check the sorting algorithms with time of running:)
    to_sort = Sorting([1,9,2,8,3,7,4,6,5])
    print("Bubble Sort")
    print(to_sort.bubble_sort())
    to_sort.asc=True
    print(to_sort.bubble_sort())
    to_sort.arr = [1,9,2,8,3,7,4,6,5]
    print("Merge Sort")
    print(to_sort.merge_sort())
    to_sort.asc = False
    print(to_sort.merge_sort())
