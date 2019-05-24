import numpy as np

f = open("sample.txt", "r")
RANGE = list(range(1,10))


lines = f.readlines()
lines = [line.replace('x', ' ').replace(',', '').strip('\n') for line in lines]
lines_fmtd = ['|'.join([line[i:i+3] for i in range(0, len(line), 3)]) for line in lines]
[print(line) for line in lines_fmtd]

board = np.array([list(line) for line in lines])

# print("Range of columns", board[:, 1:3])
rows = [board[x] for x, row in enumerate(board, 0)]
cols = [board[:, x] for x, col in enumerate(board, 0)]


# Check what numbers arent in each row:
for x, row in enumerate(rows, 0):
	for num in RANGE:
		if num not in [int(x) for x in row if x.isdigit()]:
			print("{0} not in row {1}".format(num, x))

# Check what numbers arent in each column:
for x, col in enumerate(cols, 0):
	for num in RANGE:
		if num not in [int(x) for x in col if x.isdigit()]:
			print("{0} not in col {1}".format(num, x))