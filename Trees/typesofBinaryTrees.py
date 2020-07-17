class newNode:
  def __init__(self,data,right=None,left=None):
    self.data = data
    self.right = right
    self.left = left


def isCompleteBinaryTreeIterative(root):
  '''
  A Complete binary tree is a binary tree where all the levels are filled possible except the last level, but all the nodes in the last level should be as left as possible
  '''

  #if root is None return True
  if root==None:
    return True

  queue = []
  #if we miss a child of one node
  # and found the child of the next or forthcoming nodes then
  #those are not as left as possible. To represent this we use flag.

  flag = False


  while(len(queue)!=0):

    node = queue.pop(0)


    if node.left:
      #it means that we have encountered a node with no left child
      #which means that the current level is not as left as possible. Hence not complete binary tree
      if flag==True:
        return False

      queue.append(node.left)
    else:
      #we didn't find the left child of this node,
      #if we find any child after this means
      #that they are not as left as possible
      # Hence flag is set to true
      flag = True

    if node.right:
      if flag==True:
        return False
      queue.append(node.right)
    else:
      flag=True
  return True



def isFullBinaryTree(root):
  '''
  A FullBinaryTree is a binary tree where each node has either zero children or two children
  '''
  #if root is None return True
  if root==None:
    return True

  #we have make the base condition as false one, so if it has only left or only right return false
  if (root.left==None and root.right != None) or (root.left!=None and root.left==None):
    return False

  #Now return with root.left and root.right with recursion
  return isFullBinaryTree(root.left) and isFullBinaryTree(root.right)


def isPerfectBinaryTree(root,level,d):
  '''
  A Binary tree is called perfect binary tree, if every internal node has two children, and all the leaves should be at same depth
  '''
  #if root is None it's perfect
  if root==None:
    return True

  #if it is a leaf node then check depth of that node and other leaf node
  if root.left==None and root.right==None:
    return d==level+1
  #if internal node has only one child then return False
  #since we are using return statements even leaf node give true to below
  #They won't executed since all ready those will returned by function from above if
  if root.left==None or root.right==None:
    return False
  return isPerfectBinaryTree(root.left,level+1,d) and isPerfectBinaryTree(root.right,level+1,d)


def isBalancedBinaryTree(root):
  '''
  A binary tree is called "Balanced Binary Tree", if the difference in heights of left subtree and right subtree are almost one i.e: -1,0,1
  '''
  pass


def height(root):
  #This is an helper function for isBalancedBinaryTree,
  #to find the height of the tree
  if root==None:
    return 0
  else:
    return 1+max(height(root.left),height(root.right))


def leftmostleafdepth(root):
  #This is the helper function for isPerfectBinaryTree since we need the depth of anyone leaf
  node = root
  d=0
  while(node!=None):
    d+=1
    node = node.left
  return d


if __name__=='__main__':
  root = newNode(10)
  root.left = newNode(20)
  root.right = newNode(30)

  root.left.left = newNode(40)
  root.left.right = newNode(50)
  # root.right.left = newNode(60)
  # root.right.right = newNode(70)



  d = leftmostleafdepth(root)
  print("PerfectBinaryTree: ",end="-->")
  print(isPerfectBinaryTree(root,0,d))
  print("Full Binary Tree: ",end="-->")
  print(isFullBinaryTree(root))
  print("Complete Binary Tree Iterative: ",end="-->")
  print(isCompleteBinaryTreeIterative(root))
