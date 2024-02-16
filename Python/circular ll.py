class node:
    def __init__(self,data):
        self.data  = data
        self.ref = None
class ll:
    def __init__(self):
        self.head = None

    def empty(self,data):
        if self.head is not None:
            print("not empty")
        else:
            n = node(data)
            self.head = n
            n.ref = self.head
    def traverse(self):
        if self.head is None:
            print("the linked list is emtpy")
        else:
            current = self.head
            while True:
                print(current.data)
                current = current.ref
                if current == self.head:
                    break

    def begin(self,data):
        n = node(data)
        if self.head is None:
            self.head = n
            n.ref = self.head
        else:
            current = self.head
            while current.ref != self.head:
                current =  current.ref
            n.ref = self.head
            self.head = n
            current.ref = n

    def end(self,data):
        n = node(data)
        if self.head is None:
            self.head = n
            n.ref = self.head
        else:
            current  = self.head
            while current.ref  != self.head:
                current = current.ref
            current.ref = n
            n.ref = self.head

    def after(self,data,x):
        if self.head is None:
            print("the linked list is empty")
        else:
            current  = self.head
            while True:
                if current.data == x:
                    no  = node(data)
                    no.ref = current.ref
                    current.ref = no
                    return
                current = current.ref
                if current == self.head:
                    print("not present")
                    return

    def check(self):
        if self.head is None:
            print("empty")
            return
        slow = self.head
        fast = self.head.ref
        while slow and fast.ref:
            if slow == fast or slow == fast.ref:
                print("cir ll")
                return
            slow  = slow.ref
            fast  = fast.ref.ref
        print("not ")
        return

    def delbeg(self):
        if self.head is None:
            print("the linked list is empty")
        else:
            current = self.head
            while current.ref != self.head:
                current = current.ref
            self.head = self.head.ref
            current.ref = self.head

    def delend(self):
        if self.head is None:
            print("the linked list is empty")
        else:
            current = self.head
            while current.ref.ref != self.head:
                current = current.ref
            current.ref = self.head
    def delbyvalue(self,x):
        if self.head is None:
            print("the ll is empty")
            return
        if self.head.ref == self.head:
            if self.head.data == x:
                self.head  = None
                return
            else:
                print("the element is not present")
                return
        if self.head.data == x:
            current  =  self.head
            while current.ref != self.head:
                current = current.ref
            self.head = self.head.ref
            current.ref = self.head
            return
        current = self.head
        while True:
            if current.ref.data == x:
                 current.ref = current.ref.ref
                 return
            current = current.ref
            if current.ref == self.head:
                print("the not present")
                return
