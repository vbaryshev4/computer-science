from pkgs.strings import trim, kebab_to_snake

import sys

d = {}
prev_key = None
for e in sys.argv[1:]:
    if e.startswith('-'):
        key = kebab_to_snake(trim(e, '-'))
        d[key] = True
        prev_key = key
    else:
        if prev_key != None:
            d[prev_key] = e
            prev_key = None
        else:
            raise Exception("Incorrect usage")
print(d)



