# import pkgs.tools.main

# - `max_value` - принимает именованные аргументы и 
# выводит строку вида `Max value is: <ключ> = <значение>`
# >>> max_value(a=10, b=20, c=30, d=15)
# >>> 'Max value is: c = 30'

def max_value(**kwargs):
    new_dict = dict(**kwargs)
    key, max_value = None, 0
    for i in new_dict:
        if max_value < new_dict[i]:
            key, max_value = i, new_dict[i]
    return ('{} = {}').format(key, max_value)
        

a = max_value(a=10, b=20, c=30, d=15)
print(a)

# - `arr_all` - принимает именованные аргументы 
# возвращает список списков вида `[ключей, значение]`:
# >>> arr_all(name='John', second_name='Cena')
# >>> [ ['name', 'John'], ['second_name', 'Cena'] ]

def arr_all(**kwargs):
    lst = []
    for i in kwargs:
        lst.append([i,kwargs[i]])
    return lst

b = arr_all(name='John', second_name='Cena')
print(b)





