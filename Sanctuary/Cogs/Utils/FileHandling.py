def read_file(filename:str) -> str:
	with open(filename) as a:
		return a.read()
