class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

    def appendNode(self, val: int):
        self.next = Node(val)
        self.next.prev = self


class LinkedList:
    def __init__(self):
        self.head = None
        self.__tail = None

    def __traverse(self, node: Node):
        if node is None:
            return []
        if node is self.__tail:
            return [node.val]
        list_ = self.__traverse(node.next)
        list_.append(node.val)
        return list_

    def __str__(self):
        list_ = self.__traverse(self.head)
        return " ".join([str(_) for _ in list_])

    @property
    def tail(self):
        return self.__tail.val

    def addNewNode(self, val: int):
        if self.head is None:
            self.head = Node(val)
            self.__tail = self.head
        else:
            self.__tail.appendNode(val)
            self.__tail = self.__tail.next

    def goNext(self):
        if self.head == self.__tail:
            raise ValueError("Already at the end")
        else:
            self.head = self.head.next

    def goBack(self):
        if self.head.prev is None:
            raise ValueError("Already at the start")
        else:
            self.head = self.head.prev
