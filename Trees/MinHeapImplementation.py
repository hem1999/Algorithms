class Heap:
  def parent(i):
    return (i-1)//2

  def lchild(i):
    return 2*i+1

  def rchild(i):
    return  2*i+2


def heapinsert(arr,key):
  arr.append(key)
  i = len(arr)-1
  while(i!=0 and arr[i]<arr[Heap.parent(i)]):
    arr[i],arr[Heap.parent(i)] = arr[Heap.parent(i)],arr[i]
    i = Heap.parent(i)
  return arr

def heapify(arr,i):
  smallest = i
  lc = Heap.lchild(i)
  rc = Heap.rchild(i)
  if lc< len(arr) and arr[lc]<arr[smallest]:
    smallest = lc
  if rc<len(arr) and arr[rc]<arr[smallest]:
    smallest = rc
  if smallest != i:
    arr[i],arr[smallest] = arr[smallest],arr[i]
    heapify(arr,smallest)
  return arr

def heapExtractMin(arr):
  if len(arr)==0:
    return arr,inf

  if len(arr)==1:
    k = arr.pop()
    return arr,k

  arr[0],arr[-1] = arr[-1],arr[0]
  minele = arr.pop()
  arr = heapify(arr,0)
  return arr,minele


def decreasekey(arr,ind,ele):
  if ind>len(arr):
    return inf
  arr[ind] = ele
  i=ind
  while(i!=0 and arr[i]<arr[Heap.parent(i)]):
    arr[i],arr[Heap.parent(i)] = arr[Heap.parent(i)],arr[i]
    i = Heap.parent(i)
  return arr

def delete(arr,ind):
  if ind>len(arr):
    return inf
  arr[ind],arr[-1] = arr[-1],arr[ind]
  arr.pop()
  arr = heapify(arr,ind)
  return arr

def buildHeap(arr):
  lastinternalParent = Heap.parent(len(arr)-1)
  for i in range(lastinternalParent,-1,-1):
    arr = heapify(arr,i)
  return arr


if __name__=="__main__":
  arr = [4,6,2]
  print(arr)
  arr = heapify(arr,0)
  print(arr)
  arr = heapinsert(arr,7)
  print(arr)
  # arr,minval = heapExtractMin(arr)
  # print(arr)
  # arr = decreasekey(arr,2,1)
  # print(arr)
  arr = [5,9,8,12,14,20,40]
  arr = delete(arr,1)
  print(arr)

  arr = [10,5,20,2,4,8]
  arr = buildHeap(arr)
  print(arr)
