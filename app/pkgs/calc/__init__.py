from pkgs.calc.calc import *

def run():
	while True:
		expr = input('Input expression: ')
		print('Result: ' + str(calc(expr)))