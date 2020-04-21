myarray = list(map(int,input("Please enter the list:").split()))
print("Array before sorted")
print(myarray)
if len(myarray)<=1:
    print("Already sorted")
for j in range(len(myarray)):
    swapped = False
    i=0
    while(i<len(myarray)-1):

        if myarray[i]>myarray[i+1]:
            myarray[i],myarray[i+1]=myarray[i+1],myarray[i]
            swapped=True
        i+=1
    if not swapped:
        print("Array after sorted!!")
        print(myarray)
        break;
