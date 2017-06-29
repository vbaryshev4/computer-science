## Homework 01 

#### Модуль tester

Создавть модуль под `tester` на том же уровне, что и `calc`. Этот модуль будет содержать внутри себя функции позволяющие тестировать другие модули. За основу использовать те тест-кейсы, что мы создавали на предыдущих занятиях.

Пользоваться этим модулем в других модулях можно будет примерно так: допустим рядом с модулем `string.py`, мы создаем файл `test.py`:

```python
from tester import equality_case
from string import trim

equality_case(trim('  a'), 'a', 'Should trim spaces from start of string')
equality_case(trim('a   '), 'a', 'Should trim spaces from end of string')
```

*Дополнительные задания*
 - Описать что делает код сверху
 - Придумать способ запускающий все тесты всех модулей, при условии, что файловая структура будет выглядеть так:

```
 . calc
 |--> __init__.py
 |--> calc.py
 |--> test.py 
 . string
 |--> __init__.py
 |--> string.py
 |--> test.py 
 . другой модуль
 |--> __init__.py
 |--> другой модуль.py
 |--> test.py 
```

 - Разобраться в том, что делает следующий shell-script:

```bash
TESTS=`find -E ./ -name 'test.py' -regex '.*/.*'`

if [ -z "$TESTS" ]; then
   echo "Tests not found"
fi

for i in $TESTS
do
    python "$i"
done
```

#### Задачки
Нужно реализовать следующие методы: 

 - *shuffle* - перемешивает элементы в списке
 - *kebabToSnake* - превращает строки вида `kabeab-to-snake` в `kebab_to_snake`
 - *kebabToCamel* - превращает строки вида `kabeab-to-snake` в `kebabToSnake`

```python
def shuffle(lst):
    """
        Принимает список: lst и перемешивает в нем элементы
        Возвращает другой (!sic) список. Это значит, что исходный список нельзя трогать.
    """
    pass

def kebabToSnake(string):
    pass

def kebabToSnake(string):
    pass
```