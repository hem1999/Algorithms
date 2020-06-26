myarray = [1,-3,2,1,-1]#list(map(int, input().split()))
max_current = myarray[0]
max_global = myarray[0]
for i in range(1,len(myarray)):
    max_current = max(myarray[i],max_current+myarray[i])
    max_global = max(max_current,max_global)
#Try to get the sub array
# Try to get the min subarray simailarly
print('maximum sub-array sum: '+str(max_global))
