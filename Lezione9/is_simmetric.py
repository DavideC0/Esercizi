#nodo 0 radice
#nodo i figlio a sinistra sta in posizione 2*i+1
#nodo i flio a destra sta in posizione 2*(i+1) = 2*i+2

def is_simmetric(tree: list[int]) -> bool:
    return are_mirrored(tree,1,2)

def are_mirrored(tree: list[int], left_index: int, right_index: int):
    if left_index >= len(tree) or right_index >= len(tree):
        return left_index == right_index
    
    if tree[left_index] != tree[right_index]:
        return False
    
    left_of_left = 2*left_index+1
    right_of_left = 2*left_index+2
    
    left_of_right = 2*right_index+1
    right_of_right = 2*right_index+2
    symmetric_extremes = are_mirrored(tree, left_of_left, right_of_right)
    symmetric_inner = are_mirrored(tree, right_of_left, left_of_right)
    
    return symmetric_extremes and symmetric_inner

tree = []
print(is_simmetric(tree))