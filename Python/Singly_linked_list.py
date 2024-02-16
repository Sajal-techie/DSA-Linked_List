class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "->", end=" ")
                n = n.ref
            print()

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, value):
        if self.head is None:
            print("ll is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == value:
                    break
                n = n.ref
            if n is None:
                print("value not found")
            else:
                new_node = Node(data)
                if n.ref is not None:
                    new_node.ref = n.ref
                n.ref = new_node

    def add_before(self, data, value):
        if self.head is None:
            print("linked list is empty")
        elif self.head.data == value:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == value:
                    break
                n = n.ref
            if n.ref is None:
                print("not found")
            else:
                new_node = Node(data)
                if n.ref:
                    new_node.ref = n.ref
                n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("linked list is empty ")
        else:
            if self.head.ref is not None:
                self.head = self.head.ref
            else:
                self.head = None

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_value(self, value):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.data == value:
            if self.head.ref:
                self.head = self.head.ref
            else:
                self.head = None
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == value:
                    break
                n = n.ref
            if n.ref is None:
                print("value not found")
            else:
                n.ref = n.ref.ref
    def reverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            prev = None
            curr = self.head
            while curr is not None:
                nex = curr.ref
                curr.ref = prev
                prev = curr
                curr = nex
            self.head = prev


ll = LinkedList()
ll.add_begin(4)
ll.add_begin(44)
# ll.add_end(55)
ll.add_after(33,55)
ll.display()
ll.add_before(99,4)

ll.add_end(11)
ll.add_end(55)
ll.display()
# ll.delete_begin()
# ll.delete_end()
ll.delete_value(99)
ll.display()
ll.reverse()
ll.display()

