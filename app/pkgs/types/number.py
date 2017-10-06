class Number(object):
    """docstring for Number"""

    @staticmethod
    def __get_value(inst):
        if isinstance(inst, Number):
            return inst.value
        else:
            return inst

    def __init__(self, arg):
        self.doc = "Manual"
        self.type = type(arg)
        self.value = arg
        self.changed = 0

    def __str__(self):
        return '<Number: {.value}>'.format(self)

    def __repr__(self):
        return '<Number: {.value}>'.format(self)

    def __add__(self, x):
        s = self.value + self.__get_value(x)
        return Number(s)

    def __sub__(self, x):
        s = self.value - self.__get_value(x)
        return Number(s)
    
    def __update(self):
        self.type = type(self.value)
        self.changed += 1
        return self

    def add(self, x):
        self.value += x
        return self.__update()

    def sub(self, x):
        self.value -= x
        return self.__update()

    def mul(self, x):
        self.value *= x
        return self.__update()

    def div(self, x):
        self.value /= x
        return self.__update()
