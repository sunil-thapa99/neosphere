'''
	This is Ludo game module
'''

class Ludo:
	def __init__(self, name, players=2):
		self.name = name
		self.players = players

if __name__ == '__main__':
	l = Ludo('LMAO')
	print(l.__dict__)

'''
	* import ludo
	* help(ludo)
	* o = ludo.Ludo(':O LOL')
	* o.__dict__
	* from ludo import Ludo => Import can be className or variableName or functionName. It only imports the called type. 
'''
'''
	import os
	list(os.walk(.))
	* This provides the all possible child path, directory, and filename.
	[('.', ['foldername'], ['filename']), ('./module_1', ['__pycache__'], ['chess.py', '__init__.py'])] 
'''