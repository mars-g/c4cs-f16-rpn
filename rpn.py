#!/usr/bin/env python3

import operator

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
}
def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1,arg2)
			stack.append(result)
		print(stack)


	if len(stack) != 1:
		raise TypeError("Thats too much man!")
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__== '__main__': #Note that's two underscres
	main()


