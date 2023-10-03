def is_valid_parentheses(s):
    stack = []  # Create an empty stack to store opening parentheses
    mapping = {')': '(', '}': '{', ']': '['}  # Define a mapping of closing to opening parentheses

    for char in s:
        if char in mapping:  # If the character is a closing parenthesis
            top_element = stack.pop() if stack else '#'  # Pop the top element from the stack or use '#' if stack is empty
            if mapping[char] != top_element:
                return False  # If the popped element doesn't match the corresponding opening parenthesis, return False
        else:
            stack.append(char)  # If the character is an opening parenthesis, push it onto the stack

    return not stack  # If the stack is empty after processing the entire string, it's valid

# Example usage:
if __name__ == "__main__":
    test_cases = ["()[]{}", "([{}])", "({[}])", "([)]", ""]
    
    for test_case in test_cases:
        result = is_valid_parentheses(test_case)
        print(f"{test_case}: {result}")
