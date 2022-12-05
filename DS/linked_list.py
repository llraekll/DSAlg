class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current:
            count = count+1
            current = current.next_node
        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

# This search is linear search or 0(n)

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index): 
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position >1:
                current = Node.next_node
                position -=1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node
 
    def __repr__(self) -> str:
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append('[Head: %s]' % current.data)
            elif current.next_node is None:
                nodes.append('[Tail: %s]' % current.data)
            else:
                nodes.append('[%s]' % current.data)

            current = current.next_node
        return '-> '.join(nodes)
