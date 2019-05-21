f = open("sample.txt.", "r")
lines = f.readlines()
for line in lines:
	print(line)


n = 3
lines = [line.replace('x', ' ').replace(',', '').strip('\n') for line in lines]

[print(line) for line in lines]


