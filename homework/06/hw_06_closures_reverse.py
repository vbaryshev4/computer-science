# Реверс замыкания
def times(func, num):
    print("> Times func called")

    def result(*args):
    	t = num
    	while t:
            func(*args)
            print("# Print func called")
            t -= 1

    print("> Result func about to be called")
    return result


a = times(print, 4)
a(2+2)

