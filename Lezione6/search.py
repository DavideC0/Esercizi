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