# 1. Напиши такой класс, 
# который бы получал в конструктор два списка 
# `names` и `values` и проставлял бы в качестве атрибутов 
# экземпляра имена из `names` и значения для них из `values`. Пример: 

# instance.name_1 # 'a'
# instance.name_2 # 'b' 

# _Подсказка: setattr_

class NamesAndValues(object):

    # @staticmethod
    # def dict_joiner(keys, values):
    #     if len(keys) is len(values):
    #         return {keys[i]:values[i] for i in range(len(keys))}
    #     else:
    #         raise ValueError(
    #             '''
    #             \rLenght of names = {0} 
    #             \rLenght of values = {1} 
    #             \rLenght should be equal
    #             '''.format(len(keys), len(values))
    #         )

    def __init__(self, names, values):        
        # self.dictionary = self.dict_joiner(names, values)
        if len(names) != len(values):
            raise ValueError(
                '''
                \rLenght of names = {0} 
                \rLenght of values = {1} 
                \rLenght should be equal
                '''.format(len(names), len(values))
            )

        # setattr(self, 'name_1', 'a')
        for i in range(len(names)):
            setattr(self, names[i], values[i])

    # def __getattr__(self, arg):
    #     return dic.get(arg)


instance = NamesAndValues(['name_1', 'name_2'], ['a', 'b'])
# print(instance.dictionary)
print(instance.name_1)
print(instance.name_2)


# 2. Напиши функцию, которая выводит все публичные методы заданного модуля: 

# ```python
# import module

# def print_public_methods(m):
#     pass # TODO

# print_public_methods(module)
# ```

import csv as csv
import collections as col


def get_public_methods(module):
    content = dir(module)
    for item in content:
        if callable(getattr(module, item)):
            print(item)

print(get_public_methods(csv))


# 3. Напиши функцию, которая принимает объект `obj` 
# и список строк `methods` и вызывает подряд 
# все методы имена которых соответствуют 
# (и если таковые найдутся) в `obj`:

# ```python

# class O():
#     def method_a(self):
#         print('called method A')

#     def method_b(self):
#         print('called method B')

#     def method_d(self):
#         print('called method D')

# obj = O()

# def call_all_methods(obj, methods):
#     pass # TODO

# call_all_methods(obj, ['method_a', 'method_b', 'method_c', 'method_d'])

# # called method A
# # called method B
# # called method C
# ```

# _Подсказка: hasattr, getattr_

class AllMethods(object):

    def method_a(self):
        print('called method A')

    def method_b(self):
        print('called method B')

    def method_d(self):
        print('called method D')


def call_all_methods(obj, methods):
    for method in methods:
        if hasattr(obj, method):
            getattr(obj, method)()


obj = AllMethods()
call_all_methods(obj, ['method_a',
                        'method_b',
                        'method_c',
                        'method_d'])
