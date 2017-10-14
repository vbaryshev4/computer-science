class Queue(object):
    """Queue in the list"""
    def __init__(self, limit):
        self.limit = limit
        self.items = []

    def push(self, x):
        # вставляет элемент в конец очереди
        if self.limit > len(self.items):
            self.items.append(x)
            return self

        else:
            msg = "Max count overreached: {0} of queue: {1}".format(
                self.limit,
                self.items
            )
            raise ValueError(msg)

    def pop(self): 
        # вынимает первый элемент из очереди
        if len(self.items) != 0:
            self.items.pop(0)
            return self

        else:
            msg = "No elements in {0}".format(
                self.items
            )
            raise ValueError(msg)

    def reverse(self):
        # переворачивает очередь
        self.items.reverse()
        return self

    def find(self, x):
        # ищет аргумент в очереди и возвращает его индекс
        i = self.items.index(x)
        return i

    def __len__(self):
        return len(self.items)


def test_status(x):
    print("Limit:{0}, count:{1}, list:{2}".format(
        x.limit, x.count, x.items)
    )

def test_proccess(test_name, test_limit):
    print("\nStarting of Queue testing: {0}".format(test_name))
    test_name = Queue(test_limit)
    test_status(test_name)
    test_name.push('qwe'), test_status(test_name)
    test_name.push('rty'), test_status(test_name)
    test_name.push('uiop'), test_status(test_name)
    test_name.push(123), test_status(test_name)
    test_name.push(000), test_status(test_name)
    test_name.pop(), test_status(test_name)
    test_name.pop(), test_status(test_name)
    test_name.pop(), test_status(test_name)
    test_name.pop(), test_status(test_name)
    test_name.pop(), test_status(test_name)
    test_status(test_name)
    print("End of Queue testing: {0}\n".format(test_name))
 
def run_test():
    try:
        test_proccess('A_Test', 3)

    finally:
        test_proccess('B_Test', 5)

# run_test()