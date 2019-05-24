import numpy as np

f = open("sample.txt", "r")
lines = f.readlines()
# for line in lines:
# 	print(line)

n = 3
lines = [line.replace('x', ' ').replace(',', '').strip('\n') for line in lines]
lines_fmtd = ['|'.join([line[i:i+n] for i in range(0, len(line), n)]) for line in lines]
[print(line) for line in lines_fmtd]


board = np.array([list(line) for line in lines])
[print(boardline) for boardline in board]

# board is a 2d array
# print(board[0][3])

# rows will be board[0..n][0]
# cols will be board[0][0..n]

# dont need to explicitly make rows but ok
rows = [board[i:i+1][0] for i in range(0, len(board), 1)]
[print("ROW: {0}".format(x), row) for x, row in enumerate(rows, 0)]

# fix this it doesnt work
cols = [board[0][i:i+1] for i in range(0, len(board), 1)]
[print("COL: {0}".format(x), col) for x, col in enumerate(cols, 0)]

# board_t = list(map(list, zip(*board)))
# [print("COL: {0}".format(x), col) for x, col in enumerate(board_t, 0)]


possible_nums = list(range(1,10))