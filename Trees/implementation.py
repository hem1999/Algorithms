class Node(object):
    def __init__(self,value,lchild=None,rchild=None,parent=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild
        self.parent = parent



    def isRoot(self):
        return self.parent==None

    def isInternal(self):
        return self.lchild or self.rchild

    def isExternal(self):
        return self.lchild!=None and self.rchild!=None

class BinaryTree():
    def __init__(self,root=None):
        self.root = root

    def insertNode(self,node):
        if self.root == None:
            self.root = node
        else:
             pass
#
# Height of a node is the number of edges on
 # the longest path from the node to a leaf.
#
# Depth of a node is the number of edges from the
# node to the tree's root node.
    def depth(self,node):
        print(node.value)
        if node.isRoot():
            return 0
        else:
            return 1+self.depth(node.parent)
    def depthIteration(self,node):
        pass
    def maxdepth(self,node):
        pass
    def height(self,node):
        if node.isExternal():
            return 0
        else:
            return 1+max(self.height(node.lchild),self.height(node.rchild))
    def heightIteration(self,node):
        pass
    def maxheight(self,node):
        pass
# A binary tree in which every node
# has 2 children except the leaves is
# known as a full binary tree.

    def isFullBinaryTree(self,node):

        if node is None:
            return True

        if node.lchild is None and node.rchild is None:
            return True

        if node.lchild is not None and node.rchild is not None:
            return self.isFullBinaryTree(node.lchild) and self.isFullBinaryTree(node.rchild)

        return False
    def isCompleteBinaryTree(self):
        """A binary tree which is completely filled
         with a possible exception at the bottom level
         i.e., the last level may not be completely
        filled and the bottom level is filled from left to right."""

        pass

    def isPerfectBinaryTree(self,node):
        """In a perfect binary tree, each leaf is at the
        same level and all the interior nodes have two children."""
        if node is None:
            return True

        if 1:
            pass


    def isItBinarySearchTree(self):
        #Checks if the binary tree nominates for the binary search BinaryTree
        pass

    def Preorder(self,node):
        """lchild-->parent-->rchild"""
        if node!=None:
            print(node.value,end="  ")
            self.Preorder(node.lchild)
            self.Preorder(node.rchild)

    def PostOrder(self,node):
        """rchild-->lchild-->parent"""
        if node!=None:
            self.PostOrder(node.rchild)
            self.PostOrder(node.lchild)
            print(node.value,end=" ")


    def Inorder(self,node):
        """parent-->lchild-->rchild"""
        if node!=None:
            self.Inorder(node.lchild)
            print(node.value,end=" ")
            self.Inorder(node.rchild)

    def levelOrderTraversal(self,node):
        pass

    def GivenTwoTraversalsFindTheThird(self):
        pass

    def makeBST(self):
        pass

    def largestPossibleBSTroot(self):
        pass
    def allroottoleafs(self,root,mystack):
        if root==None:
            return
        mystack.append(root.value)
        self.allroottoleafs(root.lchild,mystack)
        if root.lchild==None and root.rchild==None:
            print(mystack)
        self.allroottoleafs(root.rchild,mystack)
        mystack.pop()


    def sumofrootleaf(self,givenleaf):
        pass

    def maxofsumofrootleaf(self):
        pass

    def update(self):
        pass

    def replace(self):
        pass

    def shortestPathBetweenNodes(self):
        #There are many questions are there on the paths in leetcode
        pass
    def ancestors(self):
        #There are many questions are there on these type of ancestors
        pass
    def comparetwotrees(self,tree2):
        pass

class BinarySearchTree():

    def __init__(self,root):
        tree = BinaryTree(root)
        if tree.isItBinarySearchTree():
            self.root = root
        else:
            tree.createBinarySearchTree()
            self.root = root

    def DeleteTailNode():
        pass

    def DeleteNode():
        pass

    def isNodeExists():
        pass

    def InsertNode():
        pass



if __name__=='__main__':
    #
    # mytree:
    #         a
    #       /    \
    #      b     c
    #     / \    /
    #     d  e   f
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.lchild = b
    a.rchild = c
    b.lchild = d
    b.parent = a
    b.rchild = e
    c.parent = a
    c.lchild = f
    f.parent = c
    d.parent = b
    e.parent = b

    mytree = BinaryTree(a)
    print('Preorder Traversal: ')
    mytree.Preorder(a)
    print()
    print('PostOrder Traversal:')
    mytree.PostOrder(a)
    print()
    print('Inorder Traversal: ')
    mytree.Inorder(a)
    print(c.isExternal() and not(c.lchild and c.rchild))
    print("Is it a BinaryTree: ",end=" ")
    #if you delete node f it will be a full binary BinaryTree.
    print(mytree.isFullBinaryTree(mytree.root))

    print("Depth of node f")
    print(mytree.depth(f))

    print("All Root To Leaf Paths: ")
    mytree.allroottoleafs(a,[])
