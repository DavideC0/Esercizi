def binary_search(array: list[int], x: int) -> int:
    low: int = 0
    high: int = len(array)
    while low < high:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        else:
            if x > array[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return None

def binary_search_recursive(array: list[int], x: int) -> int:
    return __binary_search_recursive(array, x, 0, len(array))

def __binary_search_recursive(array: list[int], x: int, low: int, high: int) -> int:
    if low > high:
        return None
    mid = (low + high) // 2
    if x == array[mid]:
        return mid
    elif x > array[mid]:
        return __binary_search_recursive(array, x, mid + 1, high)
    else:
        return __binary_search_recursive(array, x, low, mid - 1)
    
def visit_tree(tree: dict[int,list[int]], node: int):
    print(node)
    left_child, right_child = tree.get(node, [None,None])
    if left_child:
        visit_tree(tree, left_child)
    if right_child:
        visit_tree(tree, right_child)

def visit_tree_iterative(tree: dict[int, list[int]], root: int):
    stack: list[int] = [root, 0]
    avg_for_level: dict[int,float] = {}
    nodes_for_level = {}
    while stack:
        curr_node, curr_level = stack.pop(0)
        
        nodes_for_level[curr_level] = nodes_for_level.get(curr_level,0) + 1

        left_child, right_child = tree.get(curr_node, [None, None])

        if left_child:
            stack.append(left_child, curr_level + 1)
            avg_for_level[curr_level] = avg_for_level.get(curr_level, 0) + left_child
        if right_child:
            stack.append(right_child)
            avg_for_level[curr_level] = avg_for_level.get(curr_level, 0) + right_child
    
    for level in avg_for_level:
        avg_for_level[level] /= nodes_for_level[level]

    return avg_for_level

tree = {4:[3,5], 3:[2,None], 5:[4.5,6], 2:[None,None], 4.5:[None,None], 6:[None,None]}
print(visit_tree_iterative(tree, 4))