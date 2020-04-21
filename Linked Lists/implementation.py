class Node(object):
    """docstring for ."""

    def __init__(self, data,nextPointer=None):
        self.data = data
        self.nextPointer = nextPointer

class LinkedList():

    def __init__(self,head=None):
        self.head = head
        self.size = 0

    def insertNode(self,node):
        self.size+=1
        if self.head==None:
            self.head = node

        else:
            cur = self.head
            while(cur.nextPointer!=None):
                cur = cur.nextPointer
            cur.nextPointer = node


    def insertFront(self,node):
        self.size+=1
        if self.head==None:
            self.head = node
        else:
            node.nextPointer=self.head
            self.head = node

    def insertTail(self,node):
        self.size+=1
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while(cur.nextPointer!=None):
                cur = cur.nextPointer
            cur.nextPointer = node

    def insertAfter(self,node,Newnode):

        if self.head == None:
            self.head = node
            self.size+=1
        else:
            cur = self.head
            while(cur.nextPointer!=None):
                if cur.data == node.data:
                    Newnode.nextPointer = node.nextPointer
                    cur.nextPointer = Newnode
                    self.size+=1
                    break
                cur = cur.nextPointer
            else:
                print("Value not found!!")

    def DeleteNode(self,value):

        if self.head==None:
            print("Nothing is there to delete")
        elif self.head.data == value:
            self.head = self.head.nextPointer
            self.size-=1
        else:
            cur = self.head
            while(cur.nextPointer!=None):
                if cur.nextPointer.data == value:
                    cur.nextPointer = cur.nextPointer.nextPointer
                    self.size-=1
                    break
                cur = cur.nextPointer
            else:
                print("Value in the list doesn't exist")
    def DeleteFirst(self):
        cur = self.head
        if self.head==None:
            print("There is nothing to remove")
        else:
            self.head = cur.nextPointer
            self.size-=1
        return cur

    def ReverseTheList(self,head):
        if head == None:
            return
        else:
            self.ReverseTheList(head.nextPointer)


    def traverseList(self):
        if self.head==None:
            print("Empty List")
        else:
            cur = self.head
            while(cur!=None):
                print(cur.data,end="-->")
                cur = cur.nextPointer
            print('None')

    def PrintreverseTraversal(self,head):
        if head==None:
            return None
        else:
            self.PrintreverseTraversal(head.nextPointer)
            print(head.data)








if __name__=='__main__':
    mylist = LinkedList()
    # mylist.traverseList()
    node1 = Node(12)
    node2 = Node(13)
    node3 = Node(14)
    print('inserting 12')
    mylist.insertNode(node1)
    mylist.traverseList()
    print(f'size of the list: {mylist.size}')
    print('inserting 13')
    mylist.insertNode(node2)
    mylist.traverseList()
    print(f'size of the list: {mylist.size}')
    print('inserting 14')
    mylist.insertNode(node3)
    mylist.traverseList()
    print(f'size of the list: {mylist.size}')
    print('inserting 15')
    mylist.insertNode(Node(15))
    mylist.traverseList()
    print(f'size of the list: {mylist.size}')
    print('deleting 14')
    mylist.DeleteNode(14)
    mylist.traverseList()
    print(f'size of the list: {mylist.size}')
    print('deleting 13')
    mylist.DeleteNode(13)
    mylist.traverseList()
    print(f'size of the list: {mylist.size}')
    print('deleting head 12')
    mylist.DeleteNode(12)
    mylist.traverseList()
    print(f'size of the list: {mylist.size}')
    print('Inserting Front 14')
    mylist.insertFront(Node(14))
    mylist.traverseList()
    print(f'size of the list: {mylist.size}')
    print('Inserting Tail 16')
    mylist.insertTail(Node(16))
    mylist.traverseList()
    print(f'size of the list: {mylist.size}')
    print('inserting tail 18')
    mylist.insertTail(Node(18))
    mylist.traverseList()
    print(f'size of the list: {mylist.size}')
    print('inserting after 16 the node 17')
    mylist.insertAfter(Node(16),Node(17))
    mylist.traverseList()
    print(f'size of the list: {mylist.size}')
    print('Reversing the list')
    mylist.PrintreverseTraversal(mylist.head)
    print('Delete First')
    print(mylist.DeleteFirst().data)
    mylist.traverseList()
    print(f'size of the list: {mylist.size}')
    # print('Reversal of Linked List')
    # print('Before reversing traversal:')
    # mylist.traverseList()
    # mylist.ReverseTheList()
    # print('After reversing the list')
    # mylist.traverseList()
