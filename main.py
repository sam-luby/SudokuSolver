import numpy as np

f = open("sample.txt", "r")
RANGE = list(range(1,10))


lines = f.readlines()
lines = [line.replace('x', ' ').replace(',', '').strip('\n') for line in lines]
lines_fmtd = ['|'.join([line[i:i+3] for i in range(0, len(line), 3)]) for line in lines]
[print(line) for line in lines_fmtd]

board = np.array([list(line) for line in lines])

# print("Range of columns", board[:, 1:3])
[print("row", x, board[x]) for x, row in enumerate(board, 0)]
[print("col", x, board[:, x]) for x, col in enumerate(board, 0)]



row1 = board[0]

row1_ints = [int(x) for x in row1 if x.isdigit()]

for num in RANGE:
	if num not in row1_ints:
		print(num, "not in row")
