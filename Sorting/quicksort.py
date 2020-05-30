from random import randrange,shuffle

class Quicksort():
    def __init__(self,arr,asc=False,every_step=True):
        self.arr = arr
        self.asc = asc
        self.every_step = every_step
        self.start = 0
        self.end = len(self.arr)-1


    def quick_sort(self):
        if self.start > self.end:
            return

        if self.every_step:
            print(f"running quick sort on {self.arr}")

        pivot_idx = randrange(self.start,self.end+1)

        pivot_element  = self.arr[pivot_idx]

        if self.every_step:
            print(f"Selected pivot is {pivot_element}")

        self.arr[self.end],self.arr[pivot_idx] = self.arr[pivot_idx],self.arr[self.end]

        less_than_pointer =  self.start #to keep track of all the elements less than the pivot_idx

        for i in range(self.start,self.end):

            if self.arr[i]<pivot_element:
                if self.every_step:
                    print(f"Swapping {self.arr[i]} with {pivot_element}")
                self.arr[i],self.arr[less_than_pointer] = self.arr[less_than_pointer],self.arr[i]
                less_than_pointer+=1
        self.arr[self.end],self.arr[less_than_pointer] = self.arr[less_than_pointer],self.arr[self.end]

        if self.every_step:
            print(f"{self.arr[self.start:self.end+1]} is sucessfully partitioned")
        self.end = less_than_pointer-1
        self.quick_sort()
        self.start = less_than_pointer+1
        self.end = len(self.arr)-1
        self.quick_sort()


if __name__=='__main__':
    qs = Quicksort([1,9,7,8,6,4,2])
    qs.quick_sort()
    print(qs.arr)
