import pprint

def solve(rawPuzzle):
	board = rawPuzzle
	location = 1, 1
	while location != None:
		location = findBlank(board)
		if location == None:
			return board

		i, j = location

		board[i][j] = -999
		print(f'{i} {j}')


def findBlank(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return i, j
	return None

def valid(board, num, row, col):
	#check row valid
	pass

def printer(board):
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print('  -  -  -   -  -  -   -  -  - ')
		for j in range(len(board[0])):
			if j % 3 == 0:
				print(f'|', end="")
			print(f" {board[i][j]} ", end="")
			if j == 8:
				print("", end="\n")


def main():

	unSolved = 	[[5,3,0,0,7,0,0,0,0],
				[6,0,0,1,9,5,0,0,0],
				[0,9,8,0,0,0,0,6,0],
				[8,0,0,0,6,0,0,0,3],
				[4,0,0,8,0,3,0,0,1],
				[7,0,0,0,2,0,0,0,6],
				[0,6,0,0,0,0,2,8,0],
				[0,0,0,4,1,9,0,0,5],
				[0,0,0,0,8,0,0,7,9]]
	solved = solve(unSolved)
	printer(solved)


if __name__ == '__main__':
	main()