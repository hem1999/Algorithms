#Let's take the simple range and solve it
#Assuming no negative values possible
arr = [1,0,9,4,3,2,6,5,8,8,8,3,3,3,2,2,2,1,1,1,7,5]
count = [0 for i in range(max(arr)+1)]
for i in arr:
    count[i]+=1
print(count)#This is the count of each element
for i in range(1,len(count)):
    count[i]= count[i]+count[i-1]
print(count)
#Let's take number 1 in the arr it's frequency is 4
#Updated count has the value 5 at index 1
#which says that the final 1 is at position 5.
output = [0 for i in arr]
for i in arr:
    output[count[i]-1]=i
    #basically at index 4 we put 1 and we decrease
    #the final index of number 1, so that the next one
    #will be at position 4 rather than position 5
    count[i]-=1
print(output)
#if we have to sort the strings we can have
#an array of 26 and do the above things


#It's been said that above algorithms works
#only for positive numbers Let's change the above
#algorithm to make it work
arr = [-1,-2,-3,-4,-4,-4,-2,-1,2,1,3,4,2,1,2,3,4]
max_el = max(arr)
min_el = min(arr)
el_rang = max_el-min_el+1
#we just map least element with 0 so that we
#can give a index to min element.
count = [0 for i in range(el_rang)]
for i in arr:
    count[i-min_el] +=1

for i in range(1,el_rang):
    count[i] = count[i]+count[i-1]

output = [0 for i in arr]
for i in arr:
    output[count[i-min_el]-1]=i
    count[i-min_el]-=1
print(output)
