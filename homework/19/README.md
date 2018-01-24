# 19

## Класс TestCase

1. Нужно расширить класс TestCase дополнив его методами сравнений:

 - `to_smaller_then` - если данное значение меньше указанного. Пример:

```python
TestCase('3 should be smaller than 10').expect(3).to_smaller_then(10)
```

 - `to_raise(Error)` - если вызов переданной функции бросает ошибку. Пример:

```python

def error_function():
	return 1 + '1' # это выбросит TypeError

TestCase('Should raise error').expect(error_function).to_raise(TypeError)
```

 - `to_be_type(type)` - если данное значение того же тика, что `type`

```python
TestCase('3 type of int').expect(3).to_be_type(int)
```

 - `to_be_instance_of(Class)` - если данное значение является экземплером `Class`

```python
TestCase('array should be instance of list').expect([1, 2, 3]).to_be_instance_of(list)
```

 - `to_has_attr('attr')` - если данное значение имеет атрибут `attr`

```python
class A:
	x = 10

TestCase('object should have attribute x').expect(A()).to_has_attr('x')
```

 - `to_has_method('method')` - если данное значение имеет метод `method`
```python
TestCase('list instance should have method append').expect([]).to_has_method('append')
```

2. Избавиться от дублирования кода

3. Добавить спец-свойство `.not` - после которого в chaining можно вызвать любой из вышеперечисленных методов и получить обратный предикат. Пример: 

```
TestCase('3 should not to be smaller than 1').expect(3).not.to_smaller_then(1)
```

4. Продумать возможность как сделать так, чтобы можно было в тесткейсе указывать двойные условия. Сейчас предикаты выглядят одинарно: X должен соответствовать условию A. А хотелось бы иметь возмжность указать: X должен соответствовать условиям A, B и C. Нужно продумать как будет выглядеть результат теста и как синтаксически это должно выглядеть в рамказ методов класса TestCase. 

