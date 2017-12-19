# 18

## Атрибуты

1. Напиши такой класс, который бы получал в конструктор два списка `names` и `values` и проставлял бы в качестве атрибутов экземпляра имена из `names` и значения для них из `values`. Пример: 

```python
class MyClass():
    pass # TODO


instance = MyClass(['name_1', 'name_2'], ['a', 'b'])

instance.name_1 # 'a'
instance.name_2 # 'b' 
```

_Подсказка: setattr_


2. Напиши функцию, которая выводит все публичные методы заданного модуля: 

```python
import module

def print_public_methods(m):
    pass # TODO

print_public_methods(module)
```

_Подсказка: dir_

3. Напиши функцию, которая принимает объект `obj` и список строк `methods` и вызывает подряд все методы имена которых соответствуют (и если таковые найдутся) в `obj`:

```python

class O():
    def method_a(self):
        print('called method A')

    def method_b(self):
        print('called method B')

    def method_d(self):
        print('called method D')

obj = O()

def call_all_methods(obj, methods):
    pass # TODO

call_all_methods(obj, ['method_a', 'method_b', 'method_c', 'method_d'])

# called method A
# called method B
# called method C
```

_Подсказка: hasattr, getattr_
