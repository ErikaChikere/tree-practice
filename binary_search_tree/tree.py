class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
        


class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)

    def add(self, key, value = None):
        if self.root == None: 
            self.root = TreeNode(key,value)
        else: 
            self.add_helper(self.root, key, value=None)

    def add_helper(self, current_node, key, value): 
        if current_node == None:
            return TreeNode(key,value)
        if key < current_node.key:
            current_node.left = self.add_helper(current_node.left,key, value)
        else: 
            current_node.right = self.add_helper(current_node.right,key,value)
        
        return current_node
               

    # Time Complexity: O(log n)
    # Space Complexity: O(log n)

    def find(self, key):
        return self.find_helper(self.root, key)
        
    def find_helper(self,current, key):
        if current == None: 
            return None
        
        if current.key == key: 
            return self.find_helper(current.left, key)

        return self.find_helper(current.right, key)
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    #Inorder: processes the root after the traversal of left child and before the traversal of right child.
    def inorder(self):
        return self.inorder_helper(self.root)

    def inorder_helper(self, current):
        order = []
        if current:
            order = self.inorder_helper(current.left)
            order.append({'key': current.key, 'value': current.value})
            order = order + self.inorder_helper(current.right)
        return order

    # Time Complexity: O(n)
    # Space Complexity: O(h)

    #Preorder: processes the root before the traversals of left and right children.  
    def preorder(self):
        return self.preorder_helper(self.root)
    
    def preorder_helper(self, current):
        order = []
        if current:
            order.append({'key': current.key, 'value': current.value})
            order = order + self.preorder_helper(current.left)
            order = order + self.preorder_helper(current.right)

        return order

    # Time Complexity: O(n)
    # Space Complexity: O(n) 

    #Postorder: processes the root after the traversals of left and right children. 
    def postorder(self):
        return self.postorder_helper(self.root)

    def postorder_helper(self, current):
        order = []
        if current:
            order = self.postorder_helper(current.left)
            order = order + self.postorder_helper(current.right)
            order.append({'key': current.key, 'value': current.value})

        return order

    # Time Complexity: O(n)
    # Space Complexity: O(h) 
    def height(self):
        return self.height_helper(self.root)

    def height_helper(self, current):
        height = 0

        if current:
            height = 1 + max(self.height_helper(current.left), self.height_helper(current.right))

        return height 


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
