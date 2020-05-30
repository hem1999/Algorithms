
class InsertionSort():

    def __init__(self,arr,asc=False,every_step=True):
        self.arr = arr
        self.asc = asc
        self.every_step = every_step

    def insertion_sort(self):
        '''
        Something about insertion sort.

        '''
        for i in range(1,len(self.arr)):

            key = self.arr[i]

            j = i-1

            while(j>=0 and key<=self.arr[j]):
                self.arr[j+1]=self.arr[j]
                j-=1
                if self.every_step:
                    self.print_array()
            self.arr[j+1] = key

    def print_array(self):
        print(self.arr)

if __name__=='__main__':
    ins = InsertionSort(arr = [1,9,8,2,7,3])
    ins.insertion_sort()
    print("################")
    ins.print_array()
