class Node:
    def __init__(self,value,left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def all_paths_for_sum():
    # return
    allPaths = []
    root_to_leaf_path(root,[], allPaths, sum)
    return allPaths

def root_to_leaf_path (currentNode , currentPath, allPaths, sum):
    #edge case
    if currentNode is None:
        return []

    ## add node to path
    currentPath.append(currentNode.value)

    #if it is a leaf check is current sum = sum
    if currentNode.value == sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(currentPath)

    else:
        # traverse left sub tree  track current path and if sum matches s then store in the allPaths array
        root_to_leaf_path(currentNode.left, currentPath, allPaths, sum - currentNode.value)

        # traverse right sub tree track current path and if sum matches s then store in the allPaths array
        root_to_leaf_path(currentNode.right, currentPath, allPaths, sum - currentNode.value)

    # when reach node back track to all recursion to continue
    del currentPath[-1]
def main ():
    root = Node(1)
    root.left = Node(7)
    root.right = Node(9)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(2)
    root.right.right = Node (7)

main ()