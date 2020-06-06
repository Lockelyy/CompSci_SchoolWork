class Node:
    def __init__(self, name, enterMessage):
        self.name = name
        self.next = None
        self.enterMessage = enterMessage

    def desc(self):
        print(self.enterMessage)

    def return_name(self):
        return self.name


class LinkedList:
    def __init__(self):
        self.head = None

    def iter(self):
        node = self.head
        while node is not None:
            print(node)
            node = node.next

    def next_room(self):
        node = self.head





