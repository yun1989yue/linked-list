class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import Queue
q = Queue.Queue()
input = [1,2,10,3,8,11,'#',4,5,'#',9]
root = TreeNode(input[0])
q.put(root)
start = 1
while start < len(input):
    temp = q.get()
    if input[start] != '#':
        temp.left = TreeNode(input[start])
        q.put(temp.left)
    start += 1
    if input[start] != '#':
        temp.right = TreeNode(input[start])
        q.put(temp.right)
    start += 1
    
def morri(root):
    if not root:
        return None
    if root.left:
        nextNode = root.left
        ex = root.left
        while ex.right:
            ex = ex.right
        ex.right = root
        root.left = None
        root.right = morri(root.right)
        return morri(nextNode)
    elif root.right:
        root.right = morri(root.right)
        return root
    else:
        return root

output = morri(root)
while output:
    print output.val
    output = output.right
