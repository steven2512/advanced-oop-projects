"""
    SortedList ADT.
    Defines a generic abstract sorted list with the standard methods.
    Items to store should be of time ListItem.
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')
K = TypeVar('K')

__author__ = 'Nguyen Duong'
__docformat__ = 'reStructuredText'

class ListItem(Generic[T, K]):
    """ Items to be stored in a list, including the value and the key used for sorting. """
    def __init__(self, value: T, key: K):
        self.value = value
        self.key = key

    def __str__(self) -> str:
        return '({0}, {1})'.format(self.value, self.key)

class SortedList(ABC, Generic[T]):
    """ Abstract class for a generic SortedList. """
    def __init__(self) -> None:
        """ Basic SortedList object initialiser. """
        self.length = 0

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        pass