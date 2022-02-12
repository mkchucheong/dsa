from treeClass import Node

def inorder_traversal(root):
    out_arr = []

    def traverse(out_arr, root):
        if root is None:
            return
        
        traverse(out_arr, root.left)
        out_arr.append(root.data)
        print(root.data)
        print(out_arr)
        traverse(out_arr, root.right)
        return out_arr
    
    return traverse(out_arr, root)

def preorder_traversal(root):
    out_arr = []

    def traverse(out_arr, root):
        if root is None:
            return
        
        out_arr.append(root.data)
        print(out_arr)
        traverse(out_arr, root.left)
        traverse(out_arr, root.right)

        return out_arr
    
    return traverse(out_arr, root)

def postorder_traversal(root):
    out_arr = []

    def traverse(out_arr, root):
        if root is None:
            return
        
        traverse(out_arr, root.left)
        traverse(out_arr, root.right)
        out_arr.append(root.data)
        print(out_arr)
        return out_arr
    
    return traverse(out_arr, root)


if __name__== "__main__":
    #     6
    #   3   8
    #  1 4 7 9
    root = Node(6)
    leaf1 = Node(1)
    leaf2 = Node(4)
    leaf3 = Node(7)
    leaf4 = Node(9)
    leaf5 = Node(3)
    leaf6 = Node(8)

    leaf5.insertLeftNode(leaf1)
    leaf5.insertRightNode(leaf2)

    leaf6.insertLeftNode(leaf3)
    leaf6.insertRightNode(leaf4)

    root.insertLeftNode(leaf5)
    root.insertRightNode(leaf6)

    print(postorder_traversal(root))
