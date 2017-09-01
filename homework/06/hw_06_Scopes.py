# Почитать про области видимости
	# https://foxford.ru/wiki/informatika/oblasti-vidimosti-peremennyh-v-python

# Что такое предопределенные имена в модуле builtins)?

# Результат чтения
#Пример №1

# Перемнные бывает трех видов: 
	# глобальная
	# локальная если объявляется в пределах конструкции def
	# не локальная

A = 1 # глобальная. Одинаково вызывается для fn() и local_fn()

def fn():
	b = 100 # не локальная для local_fn
	print(b)

	def local_fn():
		c = 1000 # локальная для local_fn
		print(c)
		global z # объявляем локальную переменную глобальной
		z = 4
		# nonlocal var ????
		# var = 666 ????


	c = 9999
	local_fn()
	print(c) # не локальная для local_fn

B = 2 # глобальная. Одинаково вызывается для fn() и local_fn()

fn()
print(z)


'''
Пример №2

# Функции образуют локальную область видимости, а модули – глобальную.

a = 10
Z = 111


def fn():
    print(a) # сработает вызов глобальной переменной a
    b = 20 # b – локальная переменная. Выводится на экран только при вызове функции.
    print(b) # сработает вызов b
    print(Z) # сработает вызов Z, хотя она объявлена после fn()

Z = 666 # Z перетерает значение

fn() # вызовет a и b
print(a) # повторный прямой вызов a
print(b) # не сработает вызов b, поскольку b находится в облости видимости def fn()
'''