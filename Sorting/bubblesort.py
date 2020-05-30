
class Bubblesort():
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

if __name__=='__main__':
    bs = Bubblesort([1,9,4,5,8,7,62])
    print(bs.bubble_sort())
