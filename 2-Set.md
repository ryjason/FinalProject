# 2. Set

## Introduction:
In the world of data structures, a set stands as a cornerstone, representing an unordered collection of unique elements. As we embark on this journey, we'll unravel the essence of sets and their mathematical properties, paving the way for efficient data manipulation.

## Definition of a Set (Unordered collection of unique elements):
A set is a fundamental data structure that represents a collection of unique elements, devoid of any specific order. Each element within a set is distinct, ensuring uniqueness throughout.
![](Picture%20Files/Weixin%20Image_20240330150154.jpg)

## Mathematical properties of Sets:
Sets unleash a treasure trove of mathematical operations, enabling us to manipulate data with finesse:

Union: Combining two sets to form a new set containing all unique elements from both sets.
Intersection: Extracting the common elements shared between two sets, forming a new set.
Difference: Subtracting one set from another, resulting in a set containing elements present in the first set but not in the second.

## Real-world examples of sets:
We can always using set data structure to remove the duplicates from a list. As one the characteristic of set is "a collection of unique elements."
```python
# Sample list with duplicates
my_list = [1, 2, 3, 4, 5, 2, 3, 4, 5]

# Create an empty set
my_set = set()

# Add elements from the list to the set
for element in my_list:
    my_set.add(element)

# Print the resulting set
print(my_set)
```
Return:
```python
{1, 2, 3, 4, 5}
```

## Operations:
1. Add: Inserting an element into the set, ensuring uniqueness by disregarding duplicates.
   - Time Complexity: O(1) on average for a hash set, O(log n) for a balanced tree set in terms of comparisons, where n is the number of elements in the set.
   - Explanation: In a hash set, adding an element typically involves computing the hash of the element and inserting it into a bucket in constant time, assuming a good hash function and minimal collisions. In a balanced tree set, adding an element requires traversing the tree to find the appropriate position, which takes O(log n) comparisons in a balanced tree.
2. Remove: Deleting a specified element from the set, if it exists.
   - Time Complexity: O(1) on average for a hash set, O(log n) for a balanced tree set in terms of comparisons, where n is the number of elements in the set.
   - Explanation: Similar to the add operation, removal in a hash set involves locating the element in a bucket and removing it in constant time. In a balanced tree set, removal also requires traversing the tree to find the element, which takes O(log n) comparisons in a balanced tree.
3. Contains: Verifying whether a specific element exists within the set.
   - Time Complexity: O(n) on average for a hash set, O(log n) for a balanced tree set in terms of comparisons, where n is the number of elements in the set.
   - Explanation: In a hash set, checking for containment involves computing the hash of the element and looking it up in the appropriate bucket, typically in constant time. In a balanced tree set, containment checking requires traversing the tree to find the element, which takes O(log n) comparisons in a balanced tree.
4. Size: Determining the cardinality of the set, i.e., the number of elements it contains.
   - Time Complexity: O(n)
   - Explanation: Most set implementations maintain a variable to keep track of the number of elements in the set. Accessing this variable takes constant time.

## Example (To Use All the Operations):
```python
class MySet:
   def __init__(self):
      self.elements = set()

   def add_element(self, element):
      self.elements.add(element)

   def remove_element(self, element):
      if element in self.elements:
         self.elements.remove(element)

   def contains_element(self, element):
      return element in self.elements

   def get_size(self):
      return len(self.elements)


# Example usage:
my_set = MySet()

my_set.add_element(5)
my_set.add_element(10)
my_set.add_element(5) 

print("Set:", my_set.elements)
print("Size of set:", my_set.get_size())

my_set.remove_element(10)
print("Set after removing 10:", my_set.elements)
print("Size of set after removing 10:", my_set.get_size())

print("Does the set contain 5?", my_set.contains_element(5))
print("Does the set contain 10?", my_set.contains_element(10))
```
Return:
```python
Set: {10, 5}
Size of set: 2
Set after removing 10: {5}
Size of set after removing 10: 1
Does the set contain 5? True
Does the set contain 10? False
```

## Problem to Solve (Library System):
Your task is to complete the methods (add_book, remove_book, display_books, is_book_available, count_books) of the Library class to implement the features described in the problem statement. Use sets to efficiently manage the collection of books in the library.

Starter code:
```python
class Library:
    def __init__(self):
        self.books = set()

    def add_book(self, book):
        """
        Add a book to the library.
        """
        pass

    def remove_book(self, book):
        """
        Remove a book from the library.
        """
        pass

    def display_books(self):
        """
        Display all the books in the library.
        """
        pass

    def is_book_available(self, book):
        """
        Check if a specific book is available in the library.
        """
        pass

    def count_books(self):
        """
        Count the total number of books in the library.
        """
        pass

# Example usage:
library = Library()

library.add_book("Harry Potter and the Sorcerer's Stone")
library.add_book("The Great Gatsby")
library.add_book("To Kill a Mockingbird")

print("Books in the library:")
library.display_books()

print("\nRemoving 'The Great Gatsby' from the library.")
library.remove_book("The Great Gatsby")

print("\nBooks in the library after removal:")
library.display_books()

print("\nIs 'To Kill a Mockingbird' available in the library?")
print(library.is_book_available("To Kill a Mockingbird"))

print("\nTotal number of books in the library:", library.count_books())
```
[Answer](Python%20Files/setanswer.py)

[Back](./README.md)