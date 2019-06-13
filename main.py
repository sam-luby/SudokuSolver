import numpy as np

RANGE = list(range(1,10))


def create_board(filename):
	f = open(filename, 'r')
	lines = f.readlines()
	lines = [line.replace('x', ' ').replace(',', '').strip('\n') for line in lines]
	lines_fmtd = ['|'.join([line[i:i+3] for i in range(0, len(line), 3)]) for line in lines]
	board = np.array([list(line) for line in lines])
	return board

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

# Gets the index rages for a given block
# 	eg in block one, row and column indexes are [0,1,2]
def get_block_indexes(block):
	if block == 1:
		return range(0,3), range(0,3)
	if block == 2:
		return range(0,3), range(3,6)
	if block == 3:
		return range(0,3), range(6,9)
	if block == 4:
		return range(3,6), range(0,3)
	if block == 5:
		return range(3,6), range(3,6)
	if block == 6:
		return range(3,6), range(6,9)
	if block == 7:
		return range(6,9), range(0,3)
	if block == 8:
		return range(6,9), range(3,6)
	if block == 9:
		return range(6,9), range(6,9)

# returns a list of present missing numbers in a row
def get_present_missing_numbers_row(row, board):
	missing_numbers = []
	present_numbers = [int(x) for x in board[row] if x.isdigit()]
	missing_numbers = list(set(RANGE) - set(present_numbers))

	numbers = 	{"present": present_numbers,
				"missing": missing_numbers}
	return numbers

# returns a list of present missing numbers in a column
def get_present_missing_numbers_column(column, board):
	missing_numbers = []
	present_numbers = [int(x) for x in board[:, column] if x.isdigit()]
	missing_numbers = list(set(RANGE) - set(present_numbers))

	numbers = 	{"present": present_numbers,
				"missing": missing_numbers}
	return numbers

# returns a list of present and missing numbers in a given 3x3 block
def get_present_missing_numbers_in_block(block, board):
	missing_numbers = []
	numbers_present = []
	numbers = {}

	row_indexes, column_indexes = get_block_indexes(block)

	for row_index in row_indexes:
		for column_index in column_indexes:
			if board[row_index][column_index].isdigit():
				numbers_present.append(board[row_index][column_index])
	
	for num in RANGE:
		if num not in [int(x) for x in numbers_present if x.isdigit()]:
			missing_numbers.append(num)

	numbers["present"] = numbers_present
	numbers["missing"] = missing_numbers
	return numbers

def check_number_not_in_row_and_column(num, proposed_loc, board):
	nums_in_row = get_present_missing_numbers_row(proposed_loc[0], board)["present"]
	nums_in_col = get_present_missing_numbers_column(proposed_loc[1], board)["present"]

	if num not in nums_in_row and num not in nums_in_col:
		return True
	return False


board = create_board('sample.txt')
print(board)

# print("Range of columns", board[:, 1:3])
rows = [board[x] for x, row in enumerate(board, 0)]
cols = [board[:, x] for x, col in enumerate(board, 0)]


## tests
for row_num in range(0,9):
	print("\nMissing numbers in row {0}:".format(row_num),
		get_present_missing_numbers_row(row_num, board)["missing"])
	print("Present numbers in row {0}:".format(row_num),
		get_present_missing_numbers_row(row_num, board)["present"])

for col_num in range(0,9):
	print("\nMissing numbers in col {0}".format(col_num),
		get_present_missing_numbers_column(col_num, board)["missing"])
	print("Present numbers in col {0}".format(col_num),
		get_present_missing_numbers_column(col_num, board)["present"])

for x in range(1, 9):
	missing_nums = get_present_missing_numbers_in_block(x, board)["missing"]
	print("Missing numbers in block {0}: {1}".format(x, missing_nums))


print(check_number_not_in_row_and_column(1, [1,1], board))
