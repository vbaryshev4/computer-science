"""
    >>> flatten([1, [2, [3, [4]], 5]]);
    [1, 2, 3, 4, 5]
"""

# code from: def change_last_item
arr = [1, [2, [3, [4]], 5]]
print("List at begin =", arr)


last = arr[-1]
print("Last before while cycle =", last)
stack = []
print("Stack before while cycle =", stack)

while isinstance(last, list):
    stack.append(last)
    print("Stack inside while cycle =", stack)
    last = last[-1]
    print("Last inside while cycle =", last)

stack.append(last)    
print("Stack after while cycle =", stack)

stack.reverse()
print("Stack after reverse =", stack)

prev = None

for i in stack:
    if not isinstance(i, list):
        # arr.pop(prev)
        prev = None
        print("Prev after if not statement =", prev)
    else:
        i[-1] = prev
        print("i[-1] after else statement =", i[-1]) 
        prev = i
        print("Prev after else statement =", prev)

arr[-1] = prev
print("i[-1] after all =", arr[-1]) 
print("Arr after all =", arr)