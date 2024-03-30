# 1. Stack

## Introduction:
A stack is a fundamental data structure that operates on the principle of Last In, First Out (LIFO). Picture a stack of plates in a cafeteria: the last plate placed onto the stack is the first one to be removed. In this section, we'll explore the definition of a stack and its real-world applications.

## Definition of a Stack (LIFO - Last In, First Out):
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means that the last element added to the stack will be the first one to be removed.
![](Picture%20Files/Weixin%20Image_20240322192537.jpg)

## Real-world examples of stacks:
Stacks are ubiquitous in both the digital and physical worlds. Consider the Undo/Redo functionality in text editors or graphic design software. Each action performed is added to a stack, allowing users to backtrack through their history. Similarly, in programming, the call stack manages function calls during program execution, ensuring that each function call is processed in the reverse order of its invocation.
```python
stack = []
//add 1,2,3 to the list
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size()) // 3
print("Top of the stack:", stack.peek()) // Output 3
print("Popped item:", stack.pop()) // Output 
```

## Operations:
1. Push: Adding an element to the top of the stack.
   - Time Complexity: O(1)
   - Explanation: Since you're adding the element to the top of the stack, regardless of the size of the stack, the time taken is constant.
2. Pop: Removing and returning the top element from the stack.
   - Time Complexity: O(1)
   - Explanation: Similar to push, popping from the top of the stack can be done in constant time, regardless of the stack's size.
3. Size: Returning the number of elements currently in the stack.
   - Time Complexity: O(1)
   - Explanation: To keep track of the number of elements in the stack, most implementations maintain a variable that stores this count. Accessing this count variable takes constant time.
4. Empty: Checking if the stack is empty.
   - Time Complexity: O(1)
   - Explanation: Similar to the size operation, checking whether the stack is empty typically involves examining a single variable or condition, which can be done in constant time.

## Example (Reverse String):
Stack is implemented using a Python list. The Stack class has methods for pushing elements onto the stack (push), popping elements off the stack (pop), checking if the stack is empty (is_empty), getting the top element of the stack without removing it (peek), and getting the size of the stack (size).

The reverse_string function takes a string as input, initializes an empty stack, pushes each character of the string onto the stack, and then pops each character off the stack to construct the reversed string.

The example usage demonstrates how to use the reverse_string function to reverse a string.

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

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

    def size(self):
        return len(self.items)

def reverse_string(string):
    stack = Stack()
    reversed_string = ""
    for char in string:
        stack.push(char)
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string

string_to_reverse = "Hello, world!"
print("Original string:", string_to_reverse)
print("Reversed string:", reverse_string(string_to_reverse))
```

## Problem to Solve (Checks Balanced Parentheses):
Your task it to complete the check_balanced_parentheses() function. Function takes an expression containing parentheses as input and checks if the parentheses are balanced using a stack. It iterates through each character in the expression, pushing opening parentheses onto the stack and popping them off when encountering a corresponding closing parenthesis. If the stack is empty at the end, it means all parentheses were balanced.

```python
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
    pass    
    #Your answer here



expression1 = "((2 + 3) * [5 - 4])"
expression2 = "{[()()]}"
expression3 = "({)}"
print("Expression 1:", "Balanced" if check_balanced_parentheses(expression1) else "Not balanced")
print("Expression 2:", "Balanced" if check_balanced_parentheses(expression2) else "Not balanced")
print("Expression 3:", "Balanced" if check_balanced_parentheses(expression3) else "Not balanced")
```
[Answer](Python%20Files/stackanswer.py)

[Back](./README.md)
