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

	numbers = {"present": present_numbers,
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

	numbers = {"present": numbers_present,
			"missing": missing_numbers}
	return numbers

# checks if a given number in a proposed location clashes horizontally/vertically (row/column) 
#	or in the same block as an existing number (i.e. checks if it is a valid location)
def check_number_not_in_row_and_column_and_block(num, proposed_loc, board):
	nums_in_row = get_present_missing_numbers_row(proposed_loc[0], board)["present"]
	nums_in_col = get_present_missing_numbers_column(proposed_loc[1], board)["present"]
	block = get_block_region(proposed_loc[0], proposed_loc[1])
	nums_in_block = get_present_missing_numbers_in_block(block, board)["present"]

	if num not in nums_in_row and num not in nums_in_col and num not in nums_in_block:
		return True
	return False

# checks if, for a given number and location, the number is in the other two 
#	rows/columns in the adjacent blocks
def check_number_present_in_adjacent_rows_columns(num, proposed_loc, board):

	# get block number
	block_num = get_block_region(proposed_loc[0], proposed_loc[1])

	# get block indexes
	row_indexes, col_indexes = get_block_indexes(block_num)
	present = {}

	# check if the proposed number is in the other 2 rows/columns for adjacent blocks
	for index in [index for index in row_indexes if index is not proposed_loc[0]]:
		present_nums = get_present_missing_numbers_row(index, board)["present"]
		present.update({"row{0}".format(index): True if num in present_nums else False})

	for index in [index for index in col_indexes if index is not proposed_loc[1]]:
		present_nums = get_present_missing_numbers_column(index, board)["present"]
		present.update({"col{0}".format(index): True if num in present_nums else False})

	return present
	

# checks if a given number in a proposed location is the ONLY valid choice
def check_if_unique_number_exists(proposed_loc, board):
	valids = {}

	# check if theres is only one valid number for location
	for x in range(1, 10):
		valids.update({"{0}".format(x): check_number_not_in_row_and_column_and_block(x, proposed_loc, board)})

	# only unique if it is the only valid number that can go in the location
	unique = (True if sum(value is True for value in valids.values()) is 1 else False)
	if unique:
		for num, valid in valids.items():
			if valid is True:
				return unique, num
	return unique, None


# checks every location on board to see if a unique solutions exists
def check_every_loc(board):
	uniques = []
	for x in range(0,9):
		for y in range(0,9):
			unique, num = check_if_unique_number_exists([x, y], board)
			uniques.append(([x, y], unique, num))
	return uniques


board = create_board('sample.txt')
print(board)

# print("Range of columns", board[:, 1:3])
rows = [board[x] for x, row in enumerate(board, 0)]
cols = [board[:, x] for x, col in enumerate(board, 0)]


## tests
# for row_num in range(0,9):
# 	print("\nMissing numbers in row {0}:".format(row_num),
# 		get_present_missing_numbers_row(row_num, board)["missing"])
# 	print("Present numbers in row {0}:".format(row_num),
# 		get_present_missing_numbers_row(row_num, board)["present"])

# for col_num in range(0,9):
# 	print("\nMissing numbers in col {0}".format(col_num),
# 		get_present_missing_numbers_column(col_num, board)["missing"])
# 	print("Present numbers in col {0}".format(col_num),
# 		get_present_missing_numbers_column(col_num, board)["present"])

# for x in range(1, 9):
# 	missing_nums = get_present_missing_numbers_in_block(x, board)["missing"]
# 	print("Missing numbers in block {0}: {1}".format(x, missing_nums))


# print(check_number_not_in_row_and_column_and_block(1, [1,1], board))

# print(check_number_present_in_adjacent_rows_columns(5, [1, 1], board))

for i in range(0,100):

	uniques = check_every_loc(board)
	for e in uniques:
		if e[1] is True:
			print(e)
			loc = e[0]
			board[loc[0], loc[1]] = int(e[2])

print(board)