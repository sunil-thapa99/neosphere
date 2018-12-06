'''
	This is chess module
'''
print('Chess Game lol')
print(__name__)
def lol():
	'''
		This is lol function created to print a line. 
	'''
	print("I'm main function in module_1")

if __name__ == "__main__":
	lol()

'''
	* cat filename => shows text in terminal
	* __name__ on import gives file name but while executing file, __name__ value is __main__.
	  So, on import the function is not called. 
	* Call from different directory, from module_1 import chess
	* From same directory, import chess
	
'''