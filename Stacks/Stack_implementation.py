class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cannot pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Cannot peek at an empty stack")

    def size(self):
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack:", stack.items)  # Output: Stack: [1, 2, 3]
    print("Size of stack:", stack.size())  # Output: Size of stack: 3
    print("Top element:", stack.peek())  # Output: Top element: 3

    popped_item = stack.pop()
    print("Popped item:", popped_item)  # Output: Popped item: 3
    print("Updated Stack:", stack.items)  # Output: Updated Stack: [1, 2]
