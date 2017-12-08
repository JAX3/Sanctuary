def read_file(filename:str) -> str:
	with open(filename) as a:
		return a.read()


def write_file(filename:str, content:str) -> None:
	with open(filename, 'w') as a:
		a.write(content)
	return
