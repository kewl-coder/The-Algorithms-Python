class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head):
    if not head:
        return None
    
    slow_ptr = head  # Slow pointer moves one step at a time
    fast_ptr = head  # Fast pointer moves two steps at a time
    
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    
    return slow_ptr

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Construct a linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original Linked List:")
print_linked_list(head)

middle_node = find_middle(head)
if middle_node:
    print("Middle of the Linked List:", middle_node.val)
else:
    print("The linked list is empty.")
