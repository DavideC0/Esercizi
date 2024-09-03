class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next
    
def reverse_linked_list(head: ListNode) -> list[int]:
    values: list[int] = []
    queue: list[ListNode] = [head]
    while queue:
        currentNode: ListNode = queue.pop()
        if currentNode:
            values.append(currentNode.val)
            queue.append(currentNode.next)
    return values[::-1]
        
head = ListNode(val = 0, next=ListNode(val=2, next=ListNode(val=6, next=ListNode(val=-1))))

print(reverse_linked_list(head))