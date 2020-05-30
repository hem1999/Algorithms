class Sorting():
    def __init__(self,arr,asc = False):
        self.arr = arr
        self.asc = asc

    def quick_sort():
        pass

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
