# class InvalidInput(Exception):
# 	pass

# a = int(input('First Value: '))
# b = int(input('Second Value: '))
# try:
# 	if a == 1:
# 		raise InvalidInput
# 	else:
# 		print(a/b)
# except InvalidInput:
# 	print('Khai k bhayo malai :O')
# except ZeroDivisionError as e:	
# 	raise e
# except Exception:
# 	raise
# else:
# 	print('Haude Solti, try run bhayo :)')
# finally:
# 	print('hahaha k gareko hau.. Sadhai run hunchu ta ma :p')


import time
import logging

# Create logger
logging.basicConfig(filename='my_log.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()

def read_file_time(path):
	'''
		Return the content of the file at "path" and measure time required.
	'''
	start_time = time.time()
	try:
		# Read file in binary mode (rb)
		f = open(path, 'rb')
		# If file exist, make a object of file
		data = f.read()
		return data
	except FileNotFoundError as e:
		logger.error(e)
		raise
	else:
		f.close()
	finally:
		stop_time = time.time()
		dt = stop_time - start_time
		logger.info('Time required for {file} = {time}'.format(file=path, time=dt))

read_file_time('mytext.txt')