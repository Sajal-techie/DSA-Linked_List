class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class Doubly:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "->", end=" ")
                n = n.nref
            print()

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.nref = self.head
            self.head.pref = new_node
        self.head = new_node

    def reverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "->",end=" ")
                if n.nref is None:
                    break
                n = n.nref
            print("forward")
            while n is not None:
                print(n.data, '->', end=" ")
                n = n.pref

            print("reverse")

    def add_before(self, data, value):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == value:
                    break
                n = n.nref
            if n is None:
                print("value not found")
            else:
                new_node = Node(data)
                new_node.nref = n
                if n.pref:
                    new_node.pref = n.pref
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    def add_after(self, data, value):
        if self.head is None:
            print("LInked list is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == value:
                    break
                n = n.nref
            if n is None:
                print("value not found")
            else:
                new_node = Node(data)
                new_node.pref = n
                if n.nref:
                    new_node.nref = n.nref
                    n.nref.pref = new_node
                n.nref = new_node

    def delete_begin(self):
        if self.head is None:
            print("empty linked list")
        elif self.head.nref is None:
            self.head = None
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("empty linked list")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            if n.pref is None:
                self.head = None
            else:
                n.pref.nref = None

    def delete_value(self, value):
        if self.head is None:
            print("empty list")
        else:
            n = self.head
            while n is not None:
                if n.data == value:
                    break
                n = n.nref
            if n is None:
                print("not founds")
            else:
                if n.pref is None:
                    self.head = n.nref
                    self.head.pref = None
                else:
                    n.pref.nref = n.nref

                if n.nref is None:
                    n.pref.nref = None
                else:
                    n.nref.pref = n.pref


ll = Doubly()
ll.add_end(1)
ll.add_end(2)
ll.add_begin(3)
ll.add_begin(4)
ll.display()
ll.add_before(5,4)
ll.add_after(22,2)
ll.add_after(55,53)
ll.display()
ll.delete_begin()
ll.delete_end()
ll.delete_value(5)
ll.display()
ll.reverse()