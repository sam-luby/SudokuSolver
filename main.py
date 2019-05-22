f = open("sample.txt", "r")
lines = f.readlines()
# for line in lines:
# 	print(line)

n = 3
lines = [line.replace('x', ' ').replace(',', '').strip('\n') for line in lines]
lines_fmtd = ['|'.join([line[i:i+n] for i in range(0, len(line), n)]) for line in lines]
[print(line) for line in lines_fmtd]


board = [list(line) for line in lines]
[print(boardline) for boardline in board]

# board is a 2d array
print(board[0][3])

# rows will be board[0..n][0]
# cols will be board[0][0..n]



# dont need to explicitly make rows but ok
rows = [board[i:i+1][0] for i in range(0, len(board), 1)]
print("ROWS: {0}".format(rows))


# fix this it doesnt work
cols = [board[0][i:i+1] for i in range(0, len(board), 1)]
print("COLS: {0}".format(cols))