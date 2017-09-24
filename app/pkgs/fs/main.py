import os

def clear_out(lst): #Clears out of system and cache files and dirs
    result = []
    for i in lst:
        if i.startswith('.') or i.startswith('__pycache__'):
            continue
        else:
            result.append(i)
    return result


def fs_read(path): #Makes paths with a name of files and recoursive dirs
    
    result = {
        "files":[], 
        "dirs":{}
    }

    files = []
    dirs = {}

    for i in clear_out(os.listdir(path)):
        new_path = os.path.join(path,i)
        if os.path.isdir(new_path):
            dirs.update({i:fs_read(new_path)})

        elif os.path.isfile(new_path):
            files.append(i)
    
    result.update({
        "files":files,
        "dirs":dirs
    })

    return result

