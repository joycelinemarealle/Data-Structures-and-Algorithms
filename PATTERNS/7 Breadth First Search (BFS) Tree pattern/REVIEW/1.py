from collections import deque
class Node :
    def __init__(self, value, left = None, right =None):
        self.left = left
        self.right = right
        self.value = value

def traverse(root):
    result = []
    #edge case
    if root is None:
        return []

    queue = deque()
    #push root to queue
    queue.append(root)

    #loop as long queue is not empty
    while queue:
     #for each level iterate safe the levelSize
     levelSize = len(queue)
     currentLevel = [] #empty array to hold nodes of a level

    #remove levelSize nodes from queue and push to array
    for _ in range(levelSize):
        currentNode = queue.popleft()

        #add currentNode value to array
        currentLevel.append(currentNode.value)
        #when queue empty insert children in queue
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        result.append(currentLevel)
    return result

def main():
    root = Node(12)
    root.left = Node(7)
    root.right = Node(1)
    root.left.left = Node(9)
    root.right.left = Node(10)
    root.right.right = Node(5)

main ()

#push the root to a queu
#loop through queue as long as it has elements
    #3 for each iteration determine size of queue + have an empty array
    #4 remove /pop levelSize nodes from queue and push value to  add it to array --. reprents current level
    #after removing each node from queue then add children to the queue
    #if queue not empty repeat 3-5