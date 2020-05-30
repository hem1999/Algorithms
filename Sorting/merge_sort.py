class mergesort():
    def __init__(self,arr,asc = False):
        self.arr = arr
        self.asc = asc



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

if __name__=='__main__':
    ms = mergesort([1,9,2,7,8,5,6,3])
    print(ms.merge_sort())
