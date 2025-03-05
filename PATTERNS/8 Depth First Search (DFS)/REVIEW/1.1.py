class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def has_path (root,sum):
    if root is None:
        return False

    currentNode = root

    #if leaf node and current sum = S
    if sum == currentNode.value and currentNode.left is None and currentNode.right is None:
        return True

   #if not leaf call recursively on the left and right tree
    return has_path(currentNode.left, sum - currentNode.value) or has_path(currentNode.right,sum - currentNode.value)

    #do something
def main ():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node (4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print ("Tree has path " + str(has_path(root,12)))
    
    
main ()

#start from the root take it as initial node
#current_sum = s-current node value
#check if node has children recursively call function
    #track new sum
    #recurssion on both childre children
#if no children, check if current sum == s
    #return true
#if not
    #return false