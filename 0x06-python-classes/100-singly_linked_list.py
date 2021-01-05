#!/usr/bin/python3
"""
Task 100
Defines a class Node
Defines a class SinglyLinkedList
"""


class Node:
    """Has a value and a reference to the next node"""

    def __init__(self, data, next_node=None):
        """
        Initializer
        If data to be stored is not an Integer or if next_node is None
        or not a Node a TypeError exception is raised

        Args:
            data (int): data to store
            next_node (Node): reference to next Node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data stored in the node
        Returns:
            int : data in the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter for data to be stored

        If data to be stored is not an Integer a TypeError exception is raised

        Args:
            value (int): data to store
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for next_node
        Returns:
            Node: the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for the next_node
        Value must be None or type Node, otherwise a TypeError exception
        is raised

        Args:
            value (Node, None): reference to the next node
        """
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defines a Singly linked list, is printable"""

    def __init__(self):
        """Initializer, no arguments"""
        self.__head = None
        """Private attribute, no setters or getters"""

    def __str__(self):
        """String representation of a SinglyLinkedList
        Returns:
            str: string representation
        """
        s = ""
        trv = self.__head
        if trv is not None:
            s = "{:d}".format(trv.data)
            trv = trv.next_node
            while trv is not None:
                s += "\n{:d}".format(trv.data)
                trv = trv.next_node
        return s

    def sorted_insert(self, value):
        """ that inserts a new Node into the correct sorted position in the
        list (increasing order)

        Args:
            value (int): data for the new Node
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data <= value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
