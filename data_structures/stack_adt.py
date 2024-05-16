""" Stack ADT and an array implementation.

Defines a generic abstract stack with the usual methods, and implements
a stack using arrays. Also defines UnitTests for the class.
"""
__author__ = "Nguyen Duong"
__docformat__ = 'reStructuredText'

import unittest
from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from data_structures.referential_array import ArrayR, T

class Stack(ABC, Generic[T]):
    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def push(self,item:T) -> None:
        """ Pushes an element to the top of the stack."""
        pass

    @abstractmethod
    def pop(self) -> T:
        """ Pops an element from the top of the stack."""
        pass

    @abstractmethod
    def peek(self) -> T:
        """ Pops the element at the top of the stack."""
        pass

    def __len__(self) -> int:
        """ Returns the number of elements in the stack."""
        return self.length

    def is_empty(self) -> bool:
        """ True if the stack is empty. """
        return len(self) == 0

    @abstractmethod
    def is_full(self) -> bool:
        """ True if the stack is full and no element can be pushed. """
        pass

    def clear(self):
        """ Clears all elements from the stack. """
        self.length = 0