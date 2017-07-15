RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
BOLD    = "\033[;1m"
END = "\033[0;0m"

def bold(s = ''):
    return BOLD + s + END

def red(s = ''):
    return RED + s + END

def green(s = ''):
    return BOLD + GREEN + s + END

def cyan(s = ''):
    return CYAN + s + END    