class Node:
    def __init__(self, num):
        self.right = None
        self.left = None
        self.value = num
        self.size = 1

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right is  None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.value > node.value:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def find_num(tree, num):
    result = False
    if tree is None:
        return result
    if tree.value == num:
        result = True
        return result
    else:
        if tree.value > num:
            result = find_num(tree.left, num)

        elif tree.value < num:
            result = find_num(tree.right, num)
    return result


def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.value)
        print_tree(root.right)

def app_mass(tree):
    answ = []
    root = tree
    if root is None:
        pass
    else:
        answ.append(root.value)
        while root is not None:
            answ.append(root.left.value)
            answ.append(root.right.value)


def side_tree(tree):
    if tree != None:
        return (side_tree(tree.left) + 1 + side_tree(tree.right))
    else:
        return 0


def array_num(tree):
    if tree != None:
        answ = [0]*side_tree(tree)
        answ = array_help(tree, 0, answ)
        return answ
    else:
        return 0

def array_help(node_now, count, my_mass):
    if node_now != None:
        my_mass[count] = node_now.value
        my_mass = array_help(node_now.left, 2*count+1, my_mass)
        my_mass = array_help(node_now.right, 2*count+2, my_mass)
        return my_mass
    else:
        return my_mass

root = Node(8)

insert(root, Node(4))
insert(root, Node(12))
insert(root, Node(2))
insert(root, Node(1))
insert(root, Node(3))
insert(root, Node(6))
insert(root, Node(5))
insert(root, Node(7))
insert(root, Node(10))
insert(root, Node(9))
insert(root, Node(11))
insert(root, Node(14))
insert(root, Node(13))
insert(root, Node(15))

print_tree(root)
print('--------------------')
pol = find_num(root, 5)
print(f'Поиск числа 5: {pol}')
print(array_num(root))

