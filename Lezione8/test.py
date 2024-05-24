class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        
    def __str__(self) -> str:
        return f"val = {self.val} next = {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, x):
        self.head = Node(x)
        
    def get_node(self, x):
        return self.head
    
    def __str__(self) -> str:
        return f"{self.head}"
        
def has_cycle(head):
    head = Node(head)
    if not head:
            return False
        
    slow = head
    fast = head.next
        
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
        
        return False
    return False

ll1 = LinkedList()
for i in range(5):
    ll1.append(i)
node1 = ll1.get_node(1)  # Node with value 1
print(node1)
node4 = ll1.get_node(4)  # Node with value 4
print(node4)
node4.next = node1  # Creating a cycle
print(node4)

print(has_cycle(ll1.head))

"""def longest_palindrome(s: str) -> int:
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    palindrome_length = 0
    odd_count = False
    
    for count in char_count.values():
        if count % 2 == 0:
            palindrome_length += count
        else:
            palindrome_length += count - 1
            odd_count = True
    
    if odd_count:
        palindrome_length += 1
    
    return palindrome_length

        
print(longest_palindrome("abccccdd"))"""