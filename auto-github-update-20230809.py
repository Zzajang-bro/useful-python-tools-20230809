import os

def makeDirNotExist(nm):
	if not os.path.isdir(nm):
		os.mkdir(nm)