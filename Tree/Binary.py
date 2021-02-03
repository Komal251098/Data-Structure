class Node:
    #Function to create a binary tree node having given key
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key 
  
# A utility function to insert  
# a new node with the given key

# Recursive function to insert a key inti BST  
def insert(root, key):
    #if the root is None, create a node & return it 
    if root is None: 
        return Node(key) 
    else: 
        if root.val == key: 
            return root

        # if given key is less than the root node,
        # recur for right  subtree
        elif root.val < key: 
            root.right = insert(root.right, key)

        # else recur for left subtree
        else:
            # key >= root.data
            root.left = insert(root.left, key) 
    return root 
  
# A utility function to do inorder tree traversal 
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 
  
  
# Driver program to test the above functions 
# Let us create the following BST 
#    50 
#  /     \ 
# 30     70 
#  / \ / \ 
# 20 40 60 80 
  
r = Node(50) 
r = insert(r, 30) 
r = insert(r, 20) 
r = insert(r, 40) 
r = insert(r, 70) 
r = insert(r, 60) 
r = insert(r, 80) 
"""if __name__ == '__main__':
 
    r = None
    keys = [50,30,20,40,70,60,80]
 
    for key in keys:
        r = insert(r, key)"""
  
# Print inoder traversal of the BST 
inorder(r) 


