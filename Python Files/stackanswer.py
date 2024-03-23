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
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def check_balanced_parentheses(expression):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    for char in expression:
        if char in opening_brackets:
            stack.push(char)
            print(stack.items)
        elif char in closing_brackets:
            print(char)
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if (top_char == '(' and char != ')') or \
               (top_char == '[' and char != ']') or \
               (top_char == '{' and char != '}'):
                return False
    return stack.is_empty()

expression1 = "((2 + 3) * [5 - 4])"
expression2 = "{[()()]}"
expression3 = "({)}"
print("Expression 1:", "Balanced" if check_balanced_parentheses(expression1) else "Not balanced")
print("Expression 2:", "Balanced" if check_balanced_parentheses(expression2) else "Not balanced")
print("Expression 3:", "Balanced" if check_balanced_parentheses(expression3) else "Not balanced")
