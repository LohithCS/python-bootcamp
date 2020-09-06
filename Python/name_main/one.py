

print('top level in one.py')

def myfunc():
	print('myfunc in one.py')


if __name__== '__main__':
	print("one.py is being run diectly")
else:
	print("one.py has being imported")