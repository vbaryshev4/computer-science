# 09

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


