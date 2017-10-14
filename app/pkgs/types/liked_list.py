class LinkedList(object):
    """docstring for LinkedList"""
    def __init__(self, head):
        self.head = head
        self.tail = None

    def push(self, value):
        if self.tail == None:
            lst = LinkedList(value)
            self.tail = lst
        else:
            self.tail.push(value)

    def pop_trdat(self):
        pre_last = self.index(len(self) - 2)
        tail = pre_last.tail
        pre_last.tail = None
        return tail

    

    def __len__(self):
        l = 1
        current_tail = self.tail
        while current_tail != None:
            l += 1
            current_tail = current_tail.tail
        return l

    def index(self, i):
        l = 1
        current_tail = self.tail
        while current_tail != None and l <= i - 1:
            l += 1
            current_tail = current_tail.tail
        return current_tail
