class Queue(object):
    """Queue in the list"""
    def __init__(self, arg):
        self.limit = arg
        self.count = 0
        self.items = []

    def _plus_elem(self):
        if self.limit > self.count:
            self.count += 1
            return self
        else:
            msg = "Max count overreached: {0} of queue: {1}".format(
                self.count, 
                self.items
                )
            raise ValueError(msg)

    def _minus_elem(self):
        if self.count != 0:
            self.count -= 1
            return self
        else:
            msg = "No elements in {0}".format(
                self.items
                )
            raise ValueError(msg)


    def push(self, x):
        # вставляет элемент в конец очереди
        self._plus_elem()
        return self.items.append(x)

    def pop(self): 
        # вынимает первый элемент из очереди
        self._minus_elem()
        return self.items.pop(0)

    def reverse():
        # переворачивает очередь
        return None

    def find():
        # ищет аргумент в очереди и возвращает его индекс
        return None

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

run_test()

        


class Number(object):
    """docstring for Number"""

    @staticmethod
    def _get_value(inst): # Есть ли экземпляр: inst в Number. 
        if isinstance(inst, Number): 
            return inst.value # вернет значение от экз.
        else:
            return inst # вернет экземпляр, которого нет в Number
    '''
    >>> a = Number(4)

    >>> a._get_value(a.__str__)
    <bound method Number.__str__ of <Number: 4>>

    >>> a._get_value(a.div)
    <bound method Number.div of <Number: 4>>

    >>> a._get_value(a.value)
    4

    >>> a._get_value(a.doc)
    'Manual'

    >>> a._get_value(a.type)
    <class 'int'>
 
    >>> a._get_value(a.__fuck__)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'Number' object has no attribute '__fuck__'
    '''

    def __init__(self, arg): # Здесь хранятся аргументы класса
        self.doc = "Manual"
        '''
        >>> a = Number(10)
        >>> a.doc
        'Manual'

        >>> a.type
        <class 'int'>
        '''
        self.type = type(arg)
        '''
        >>> a = Number(10)
        >>> a.type
        <class 'int'>

        >>> b = Number('a')
        >>> b.type
        <class 'str'>
        '''
        self.value = arg
        '''
        >>> a = Number(10)
        >>> a.value
        10

        >>> b = Number('a')
        >>> b.value
        'a'
        '''
        self.changed = 0

    def __str__(self): # Чем отличается от __repr__ ?
        return '<Number: {.value}>'.format(self)

    def __repr__(self):
        return '<Number: {.value}>'.format(self)

    def __add__(self, x):
        s = self.value + self._get_value(x)
        return Number(s)
        '''
        >>> a = Number(10)
        >>> a
        <Number: 10>
        >>> a.__add__(3)
        <Number: 13>
        >>> a
        <Number: 10>
        '''

    def __sub__(self, x):
        s = self.value - self._get_value(x)
        return Number(s)
    
    def _update(self):
        self.type = type(self.value)
        self.changed += 1
        return self

    def add(self, x):
        self.value += x
        return self._update()
        '''
        >>> a = Number(4)
        >>> a
        <Number: 4>
        >>> a.add(6)
        <Number: 10>
        >>> a.value
        10
        >>> a.changed
        1
        '''

    def sub(self, x):
        self.value -= x
        return self._update()

    def mul(self, x):
        self.value *= x
        return self._update()

    def div(self, x):
        self.value /= x
        return self._update()
