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


# Gets the 3x3 block on the sudoku board
#   1[0:2][0:2] | 2[0:2][3:5] | 3[0:2][6:8]
#	4[3:5][0:2] | 5[3:5][3:5] | 6[3:5][6:8]
#	7[6:8][0:2] | 8[6:8][3:5] | 8[6:8][6:8]
def get_block_region(row_index, column_index):
	if row_index <= 2:
		if column_index <= 2:
			return 1
		elif column_index <= 5:
			return 2
		elif column_index <= 8:
			return 3
	elif row_index <= 5:
		if column_index <= 2:
			return 4
		elif column_index <= 5:
			return 5
		elif column_index <= 8:
			return 6
	elif row_index <=8:
		if column_index <= 2:
			return 7
		elif column_index <= 5:
			return 8
		elif column_index <= 8:
			return 9


print(get_block_region(0,0))
print(get_block_region(0,4))
print(get_block_region(0,7))
print(get_block_region(4,0))
print(get_block_region(4,4))
print(get_block_region(4,7))
print(get_block_region(7,0))
print(get_block_region(7,4))
print(get_block_region(7,7))

print(get_block_region(3,6))
print(get_block_region(7,4))

