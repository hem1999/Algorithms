
class RadixSort():
    def __init__(self,arr,asc=False):
        self.arr = arr
        self.asc = asc
        self.maxarrvalue = max(self.arr)
        self.max_exponent = len(str(self.maxarrvalue))
        self.being_sorted = self.arr[:]

    def radix_sort(self):
        for exponent in range(self.max_exponent):

            position = exponent+1
            index = -position

            digits = [[] for i in range(10)]

            for number in self.being_sorted:
                number_as_a_string = str(number)

                try:
                    digit = number_as_a_string[index]
                except IndexError:
                    digit=0
                digit = int(digit)

                digits[digit].append(number)
                print(digits)
            self.being_sorted = []
            for numeral in digits:
                self.being_sorted.extend(numeral)

        return self.being_sorted

if __name__=='__main__':
    rs = RadixSort([830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1])
    print(rs.radix_sort())
