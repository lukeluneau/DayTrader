import os

class Delete(object):
	'''
	Deletes every file in this files directory that is not a text or python file
	Exception apply
	'''
	
	def __init__(self, file):
		self.file = file

	def deleteFile(self, Ex_file = None):
		if Ex_file == self.file:
			pass
		else:
			os.remove(self.file)

if __name__ == '__main__':
	count = 0
	NASDAQ = open("NASDAQ.txt").read().splitlines()
	for file in os.listdir():
		if file.endswith(".py") != True and file.endswith(".txt") != True:
			Delete(file).deleteFile()
			count += 1
		if file[:-4] in NASDAQ:
			Delete(file).deleteFile()
		print(file[:-4])
	print("%s Graphs Deleted." % count)



