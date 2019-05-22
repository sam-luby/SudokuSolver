f = open("sample.txt", "r")
lines = f.readlines()
# for line in lines:
# 	print(line)

n = 3
lines = [line.replace('x', ' ').replace(',', '').strip('\n') for line in lines]
[print('|'.join([line[i:i+n] for i in range(0, len(line), n)])) for line in lines]
