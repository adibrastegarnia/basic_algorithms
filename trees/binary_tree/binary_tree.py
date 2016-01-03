class Node():
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self, value):
        self.val = value

    def getNodeValue(self):
        return self.val

    def insertRight(self, newNode):
        if self.right == None:
            self.right = Node(newNode)
        else:
            node = Node(newNode)
            node.right = self.right
            self.right = node

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = Node(newNode)
        else:
            node = Node(newNode)
            node.left = self.left
            self.left = node


def PreOrder(tree):
    if tree!=None:
        print(tree.getNodeValue())
        PreOrder(tree.getLeftChild())
        PreOrder(tree.getRightChild())


def Inorder(tree):
    if tree !=None:
        Inorder(tree.getLeftChild())
        print(tree.getNodeValue())
        Inorder(tree.getRightChild())

def PostOrder(tree):
    if tree !=None:
        Inorder(tree.getLeftChild())
        Inorder(tree.getRightChild())
        print(tree.getNodeValue())
            
def  main():
    myTree = Node(1)
    myTree.insertLeft(2)
    myTree.insertRight(3)
    myTree.insertRight(4)
    myTree.insertLeft(5)
    myTree.insertLeft(6)

    print("----------PreOrder----------")
    PreOrder(myTree)
    print("----------Inorder--------------")
    Inorder(myTree)
    print("----------PostOrder------------")
    PostOrder(myTree)


main()



