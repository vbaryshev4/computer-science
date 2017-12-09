# 16

## Шаблонизация данных

Предположим запуск тестов файла возвращает такую структуру данных:

```
result = {  
    'name': 'Lists Module Tests',
    'description': 'Tests for module lists',
    'file': 'lists.py',
    'path': 'pkgs.lists.lists',
    'status': True,
    'tests': [
        {
            'name': 'Shuffle test',
            'method': 'shuffle',
            'cases': [
                {
                    'arguments': [1, 2, 3, 4, 5, 6, 7],
                    'condition': {
                        'id': 'non_equality',
                        'value': [1, 2, 3, 4, 5, 6, 7]
                    },
                    'status': True,
                    'message': 'Shuffles a list with ints'
                },
                {
                    'arguments': ['a','b','c','d'],
                    'condition': {
                        'id': 'non_equality',
                        'value': ['a','b','c','d']
                    },
                    'status': True,
                    'message': 'Shuffles a list with str'
                },
                                {
                    'arguments': [1, 2, 3, 'a', 'b', 'c'],
                    'condition': {
                        'id': 'non_equality',
                        'value': [1, 2, 3, 'a', 'b', 'c']
                    },
                    'status': True,
                    'message': 'Shuffles a list with mixed'
                },
            ],
            'status': True,
        },
        {
            'name': 'Drop test',
            'method': 'drop',
            'cases': [
                {
                    'arguments': [[1, 2, 3, 1, 2, 3, 1, 2, 3], [2, 3]],
                    'result': [1, 1, 1],
                    'condition': {
                        'id': 'equality',
                        'value': [1, 1, 1]
                    },
                    'status': True,
                    'message': 'Should delete elems from list'
                },
            ]
            'status': True
        }
    ]
}
```

Нужно написать функцию, которая на вход получает эту структуру данных и рендерит следуюший HTML используя класс Tag: 

```html
<div class="container">
    <h1 class="b-heading">Lists Module Tests</h1>
    <div class="description">Tests for module lists</div>
    <div class="status">Success</div>
    <ul class="tests">
        <li class="test">
            <h4>Shuffle test</h4>
            <p>Method: <code>shuffle</code></p>
            <p class="status">Status: <code>True</code></p>
            <h5>Cases:</h5>
            <ol>
                <li class="testcase success">
                    <p class="status">Status: OK</p>
                    <p>Arguments: <code>[1, 2, 3, 4, 5, 6, 7]</code></p>
                    <div class="conditions">
                        <p class="condition-title">Conditions</p>
                        <p>ID: <code>non_equality</code></p>
                        <p>Value: <code>[1, 2, 3, 4, 5, 6, 7]</code></p>
                    </div>
                    <p>Message: Shuffles a list with ints</p>
                </li>
                <li class="testcase success">
                    <p class="status">Status: OK</p>
                    <p>Arguments: <code>['a','b','c','d']</code></p>
                    <div class="conditions">
                        <p class="condition-title">Conditions</p>
                        <p>ID: <code>non_equality</code></p>
                        <p>Value: <code>['a','b','c','d']</code></p>
                    </div>
                    <p>Message: Shuffles a list with strs</p>
                </li>
                <li class="testcase success">
                    <p class="status">Status: OK</p>
                    <p>Arguments: <code>[1, 2, 3, 'a', 'b', 'c']</code></p>
                    <div class="conditions">
                        <p class="condition-title">Conditions</p>
                        <p>ID: <code>non_equality</code></p>
                        <p>Value: <code>[1, 2, 3, 'a', 'b', 'c']</code></p>
                    </div>
                    <p>Message: Shuffles a list with mixed</p>
                </li>
            </ol>
        </li>
        <li class="test">
            <h4>Drop test</h4>
            <p>Method: <code>drop</code></p>
            <p class="status">Status: <code>True</code></p>
            <h5>Cases:</h5>
            <ol>
                <li class="testcase success">
                    <p class="status">Status: OK</p>
                    <p>Arguments: <code>[[1, 2, 3, 1, 2, 3, 1, 2, 3], [2, 3]]</code></p>
                    <div class="conditions">
                        <p class="condition-title">Conditions</p>
                        <p>ID: <code>equality</code></p>
                        <p>Value: <code>[1, 1, 1]</code></p>
                    </div>
                    <p>Message: Should delete elems from list</p>
                </li>
            </ol>
        </li>
    </ul>
</div>
```


## Часть 2: наследование от Tag

Нужно реализовать классы наследующие `Tag`, но выполняющие более специфичную работу: 

### Heading

```python
h3 = Heading(3)
h4 = Heading(4)

h3('Data') #<h3>Data</h3>
h4('Data') #<h4>Data</h4>
```


### List

```python
ordered_list = List(ordered=True, item_class_name='li-item')
unordered_list = List(ordered=False)

ordered_list(['a', 'b', 'c'], class_name='list')
'''
<ol class="list">
    <li class="li-item">a</li>
    <li class="li-item">b</li>
    <li class="li-item">c</li>
</ol>
'''

unordered_list(['a', 'b', 'c'])
'''
<ul>
    <li>a</li>
    <li>b</li>
    <li>c</li>
</ul>
'''
```

Объект класса `List` принимает список строк - которые становятся элементами списка в HTML (тэг `li`). 

List принимает именованные параметры: 
  - `ordered` - от этого зависит тэг. Если `True` - то `ol`, иначе `ul`
  - `item_class_name` - html-класс, который будет присвоен каждому элементу списка (внутренним тэгам `li`)

В остально поведение такое же как у класса `Tag`

