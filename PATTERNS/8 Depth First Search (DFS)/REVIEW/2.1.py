
class Node:
    def __init__(self, value  ,left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def has_paths(root,sum):
    allPaths = []
    #all helper
    root_to_leaf_recursive(root,[], allPaths, sum)
    return allPaths

def root_to_leaf_recursive(currentNode, currentPath, allPaths, sum):
    #edge case
    if currentNode is None:
        return #exit function so allPaths array zero

    #add currentNode onto the current path
    currentPath.append(currentNode.value)

    #if leaf node and currentNode.value == sum then store the currentPath unto the allPaths
        #return allPath.append currentPath
    if currentNode.value == sum and currentNode.left is None and currentNode.right is None:
        return allPaths.append(list(currentPath))

    #recursion on the children of currentNode
    else:
        #traverse left tree
        root_to_leaf_recursive(currentNode.left,currentPath, allPaths, sum- currentNode.value)
        # traverse right tree
        root_to_leaf_recursive(currentNode.right, currentPath,allPaths, sum-currentNode.value)
    #if leaf node but sum != currentnode.value
    #delete last element of currentPath to back track as perform up recursion stack
    del currentPath[-1]


def main ():
    root = Node(1)
    root.left = Node(7)
    root.right = Node(9)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(2)
    root.right.right = Node(7)
    print("Tree paths with sum" + str(has_paths(root,12)))
main()


#Store path if find root to leaf path
#continue checking even after first path found

  #add currentNode unto the current path
    #if leaf node and currentNode .value == sum then store the currentPath unto the allPaths
        #return allPath.append currentPath
    #recursion on the children of currentNode
    #delete last element of currentPath to back track as perform up recursion