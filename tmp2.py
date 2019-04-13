class Tree:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x
def create_tree(x,k):
    root = Tree(x)
    if root.val>0 and k>0:
        if root.val%2==0:
            k-=1
            root.left = create_tree(root.val//2,k)
            k-=1
            root.right = create_tree(root.val//2,k)
        else:
            k-=1
            root.left = create_tree(root.val//2+1,k)
            k-=1
            root.right = create_tree(root.val//2,k)
    return root
def print_root(root):
    while root!=None:
        print(root.val)
        print_root(root.left)
        print_root(root.right)
if __name__ == '__main__':
    root = create_tree(15,4)
    print_root(root)






