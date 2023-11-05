class TreeNode():
    def __init__(self, value = None) -> None:
        self.value = value
        self.childs = []

    def add_child(self, child):
        self.childs.append(child)

def create_tree(array):
    nodes = []
    for value in range(len(array)):
        nodes.append(TreeNode(value = value))

    for child_index, parent_index in enumerate(array):
        if parent_index == -1:
            root = nodes[child_index]
        else:
            nodes[parent_index].add_child(nodes[child_index])

    return root

def max_height(root):
    if root == []:
        return 0
    else:
        childs = root.childs
        max_ = 0
        for child in childs:
            max_ = max(max_, max_height(child))
        return max_ + 1

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    root = create_tree(array)
    print(max_height(root))