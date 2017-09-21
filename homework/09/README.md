# 09

### Немного про git

Посмотри на историю этой ветки. Какой командой это будет сделать удобнее?

>>> glola
```
| * b59b308 - (HEAD -> hw09, origin/hw09) Addition (7 days ago) <Trdat Mkrtchyan>
| * dc0de1d - Homework_09 (7 days ago) <Trdat Mkrtchyan>
| *   0ca9ee2 - (origin/HTTP_server) Merge pull request #9 from vbaryshev4/hw08 (7 days ago) <Trdat Mkrtchyan>
```

Что о ней [истории] можно сказать? 
```
У меня возник вопрос про HEAD. Нагуглил ответ:
A head is simply a reference to a commit object. Each head has a name (branch name or tag name, etc). By default, there is a head in every repository called master. A repository can contain any number of heads. At any given time, one head is selected as the “current head.” This head is aliased to HEAD, always in capitals".

Note this difference: a “head” (lowercase) refers to any one of the named heads in the repository; “HEAD” (uppercase) refers exclusively to the currently active head. This distinction is used frequently in Git documentation.
```

Проследи где она [ветка] возникла, 
```
dc0de1d - Homework_09 (14 сентября) <Trdat Mkrtchyan> ствол master ответвился на: master и HTTP_server. Коммит: c616c34
```

для чего произошли ответвления в истории коммитов. 
```
Ты создал последние 2 задания hw08 и hw09 в не в ветке master. Ты создал крайнюю ветку hw09 и перенес туда HEAD.
```

Сделай свое заключение о том зачем это все нужно. 
```
Чтобы не смешивать основную ветку и работу над пакетами. Допустип, сервер работает на master версии. А нам нужно сделать новую фичу. Мы делаем ответвление каждый раз, когда получаем новые задания. Потом, сливаем их в мастер. 
```

### Обход файловой структуры

Необходимо написать функцию `read_fs`, которая принимает строку - это путь к дирректории. Она обходит дирректорию рекурсивно и выводит структуру следующего вида: 

```python
{
	'files': ['__init__.py', 'a.py', 'b.py'],
	'dirs': {
		'dir1' : {
			'files': ['__init__.py', 'b.py'],
			'dirs': {
				'empty_dir': {}
			}
		},
		'dir2': {
			'files': ['one.py', 'two.py']
		}
	}
}
```

Такая структура данных соответствует следующей файловой структуре: 

```
>>> fs_read('./root')

# треугльником отмечены папки
# звездочкой файлы

> root
...> dir1
......> empty_dir #пустая папка
......* __init__.py
......* b.py
...> dir2
......* one.py
......* two.py
...* __init__.py
...* a.py
...* b.py
```

### Некоторые условия и подсказки

 - fs_read рекурсивна
 - Если fs_read передать путь до пустой дирректории - она вернет пустой список (это зерно рекурсии)
 - Внутри тела функции должно быть определения - это файл или дирректория

Тебе точно пригодятся
 - [os.listdir](https://docs.python.org/3/library/os.html#os.listdir)
 - [os.path.join](https://docs.python.org/3/library/os.path.html#os.path.join)
 - [os.path.isdir](https://docs.python.org/3/library/os.path.html#os.path.isdir)
 - [os.path.isfile](https://docs.python.org/3/library/os.path.html#os.path.isfile)


