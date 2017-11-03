# 14

## Наследование

Нужно реализовать два класса: 

 - `Resource` - класс умеющий работать с HTTP-ресурсами с методом GET
 - `API` - класс умеющий работать с HTTP-ресурсами 

Оба класса имеют аттрибут `endpoint` в котором лежит URL по которому нужно обращаться к ресурсам

### Resource

 - `get` - принимает путь до ресурса и делает туда запрос
 - `search` - принимает путь до ресурса и делает туда запрос с правильным query-string

Пример использования: 
```python

rest = Resource('http://example.com')

rest.endpoint # http://example.com

rest.get('main') # делает get-запрос на endpoint/main/
rest.search('main', foo='bar', baz='boo') # делает get-запрос на endoint/main/?foo=bar&baz=boo
```

### API

Имеет все те же аттрибуты и свойства, что экземпляр класса `Resource`, но также поддерживает методы: 

 - `post`
 - `patch`
 - `put`
 - `delete`

Которым помимо пути до ресурса можно передать тело для запроса

Пример использования:
```python
api = API('http://example.com')

api.endpoint # 'http://example.com'
api.post('resource', {
	'name': 'Vova'
}) # делает post-запрос на endpoint/resource с телом запроса {'name': 'Vova'}
```
