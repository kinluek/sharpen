class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def preorder(root):
    if root is None:
        return

    yield root.val

    for n in preorder(root.left):
        yield n

    for n in preorder(root.right):
        yield n


def create_test_tree():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n4.left = n2
    n4.right = n6

    n2.left = n1
    n2.right = n3

    n6.left = n5
    n6.right = n7

    root = n4

    return root


def test_postorder_larger_tree():
    root = create_test_tree()
    assert list(preorder(root)) == [4, 2, 1, 3, 6, 5, 7]
