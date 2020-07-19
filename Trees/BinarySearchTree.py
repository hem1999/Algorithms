class BSTNode:
  def __init__(self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right



def BSTsearch(root,key):
  if root==None:
    return False
  if key>root.data:
    return BSTsearch(root.right,key)
  elif key<root.data:
    return BSTsearch(root.left,key)
  else:
    return True


def BSTsearchIterative(root,key):
  cur = root
  while(cur!=None):
    if cur.data == key:
      return True
    elif key > root.data:
      cur = cur.right
    else:
      cur = cur.left
  return False

  
def BSTInsert(root,key):
  if root==None:
    return BSTNode(key)
  else:
    if key>root.data:
      root.right = BSTInsert(root.right,key)
    else:
      root.left = BSTInsert(root.left,key)
  return root

def BSTInsertIterative(root,key):
  newnode = BSTNode(key)
  cur = root
  parent = None
  while(cur!=None):
    parent = cur
    if key>cur.data:
      cur = cur.right
    elif key<cur.data:
      cur = cur.left
    else:
      return

  if parent == None:
    return newnode
  if key > parent.data:
    parent.right = newnode
  else:
    parent.left = newnode
  return root


def getsuccesor(root):
  root = root.right
  cur = root
  while(cur!=None and cur.left!=None):
    cur = cur.left
  return cur



def BSTdelete(root,key):
  if root==None:
    return None
  if key> root.data:
    root.right = BSTdelete(root.right,key)
  elif key<root.data:
    root.left = BSTdelete(root.left,key)
  else:
    if root.left == None:
      return root.right
    if root.right==None:
      return root.left
    node = getsuccesor(root)
    root.data = node.data
    root.right = BSTdelete(root.right,node.val)
  return root

def inorder(root):
  if root:
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)







if __name__=='__main__':
  # root = Node(10)
  # root.left = Node(90)
  # root.right = Node(9)
  # root.left.left = Node(110)

  # print(maxofBinaryTree(root))
  root = None
  root = BSTInsert(root,5)
  root = BSTInsert(root,3)
  root = BSTInsert(root,6)
  root = BSTInsert(root,2)
  root = BSTInsert(root,4)
  root = BSTInsertIterative(root,1)



  print(BSTsearch(root,6))
  inorder(root)
  print()
  print(BSTsearch(root,10))
  inorder(root)
  print()
  print(BSTsearchIterative(root,5))
  inorder(root)
  print()
  root = BSTdelete(root,1)
  inorder(root)
  print()
  print(BSTsearchIterative(root,1))
