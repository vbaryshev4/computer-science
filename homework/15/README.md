# 15

## Классы для работы с HTML

Для начала нужно немнго прочитать про HTML. Вот минимальный набор: 

```
<h1 class="title">Content</h1>
```

Здесь:
 - `h1` - это название тэга (также элемент) 
 - `class` - это имя аттрибута тэга
 - `"title"` - это значение аттрибута `class`
 - `Content` - это тело тэга 

Чтобы правильно рендерить такие HTLM-строки, нужно реализовать следующие классы:

### Tag

Общий класс всех HTML тэгов, он нам нужен для того, чтобы генерировать специальные тэги и аттрибуты этих тэгов

```python
title = Tag('h1', class_name='title') #почему class_name? потому что ключевое слово class в python уже занято

title.render('Content') # <h1 class="title">Content</h1>

title.render('Body', class_name="other") # <h1 class="other">Body</h1>

#рендеринг кастомных аттрибутов
title.render('Some', attr='value') # <h1 class="title" attr="value">Some</h1>

img = Img(class_name='img')
img.render('https://image.ru/image/name.jpg') # <img class="img" src="https://image.ru/image/name.jpg" />
```

### Вложенные тэги

```python

list = Tag('ol')

p = Tag('p')

list.render([
	p.render('One'),
	p.render('Two'),
	p.render('Three'),
])

# <ol>
#   <p>One</p>
#   <p>Two</p>
#   <p>Three</p>
# </ol>
```
