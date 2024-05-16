""" 
Lightweight array implementation using ctypes.

The __init__ function’s logic deserves clarification. The internal storage is 
created via the ctypes library, which allows defining an array of generic 
Python object references. For a given `length`, the expression 
`length * ctypes.py_object` produces a type (e.g., if length=5, the type would 
be py_object_Array_5). Calling `(length * py_object)()` allocates space for 
that many object references, similar to manual memory allocation in low-level 
languages.

Although __init__ validates the precondition (`length > 0`), bounds checking 
for __getitem__ and __setitem__ is delegated to the underlying array’s behavior.
"""

__author__ = "Julian Garcia (__init__ logic), Maria Garcia de la Banda (additional functionality)"
__docformat__ = 'reStructuredText'

from ctypes import py_object
from typing import TypeVar, Generic

T = TypeVar('T')

class ArrayR(Generic[T]):
    def __init__(self, length: int) -> None:
        """
        Initialize an array capable of holding object references.

        :complexity: O(length) to fill the array with None values.
        :precondition: length > 0
        """
        if length <= 0:
            raise ValueError("Array length must be greater than zero.")
        self.array = (length * py_object)()  # allocate array storage
        self.array[:] = [None] * length      # initialize with None

    def __len__(self) -> int:
        """
        Return the total capacity of the array.

        :complexity: O(1)
        """
        return len(self.array)

    def __getitem__(self, index: int) -> T:
        """
        Retrieve the element at a specific index.

        :complexity: O(1)
        :precondition: index must be within valid range [0, length-1]
        """
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """
        Assign a value to a specific index in the array.

        :complexity: O(1)
        :precondition: index must be within valid range [0, length-1]
        """
        self.array[index] = value

    def index(self, item: T) -> int:
        """
        Return the index of the first occurrence of `item`.

        :raises ValueError: if item is not present in the array
        :complexity: O(n) where n is array length
        """
        for idx, elem in enumerate(self.array):
            if elem == item:
                return idx
        raise ValueError("Item not found in array.")

    def __str__(self) -> str:
        """
        Return string representation of the array contents.

        :complexity: O(n) where n is array length
        """
        return "[" + ", ".join(str(item) for item in self.array) + "]"
