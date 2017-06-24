from random import randint

def shuffle(lst):
    """
        Принимает список: lst и перемешивает в нем элементы
        Возвращает другой (!sic) список. Это значит, 
        что исходный список нельзя трогать.
    """
    lst = lst.copy()
    shuffled_list = []

    while len(lst) != 0:
    	elem = randint(0, len(lst) - 1)
    	shuffled_list.append(lst[elem])
    	lst = lst[:elem] + lst[elem+1:]
    return shuffled_list

