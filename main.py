import pprint

def solve(rawPuzzle):
	board = rawPuzzle
	location = 0, 0
	while location != None:
		location = findBlank(board)
		if location == None:
			return board
		else:
			i, j = location
			print(f'Issues at {i} {j}')
			for num in range(1, 10):
				board[i][j] = num
				if valid(board, i, j):
					print(f'{num} does')
					break
				print(f'{num} does not work')

		#board[i][j] = -999
		#print(f'{i} {j}')


def findBlank(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return i, j
	return None

def valid(board, row, col):
	#check row valid
	for i in range(0, 9):
		if board[i][col] == board[row][col] and i != row:
			return False
	#check col valid
	for j in range(0, 9):
		if board[row][j] == board[row][col] and j != col:
			return False

	#check quad valid
	posRow = row//3
	posCol = col//3

	for i in range(posRow*3, posRow*3 + 3):
		for j in range(posCol*3, posCol*3 + 3):
			if board[i][j] == board[row][col] and (i,j) != (row, col):
				return False

	return True

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

	unSolved = 	[
				[5,3,0,0,7,0,0,0,0],
				[6,0,0,1,9,5,0,0,0],
				[0,9,8,0,0,0,0,6,0],
				[8,0,0,0,6,0,0,0,3],
				[4,0,0,8,0,3,0,0,1],
				[7,0,0,0,2,0,0,0,6],
				[0,6,0,0,0,0,2,8,0],
				[0,0,0,4,1,9,0,0,5],
				[0,0,0,0,8,0,0,7,9]
				]
	unsolvedTest = 	[
				[4,3,5,2,6,0,7,8,1],
				[6,0,2,5,7,1,4,9,3],
				[1,9,7,8,3,4,5,6,2],
				[8,2,6,1,9,5,3,4,7],
				[3,7,4,6,8,2,0,0,5],
				[9,0,1,7,4,3,6,2,8],
				[5,1,9,3,2,6,8,7,4],
				[2,4,8,9,5,7,1,3,6],
				[7,6,3,4,1,8,2,5,9]
				]
	
	solved = solve(unsolvedTest)
	printer(solved)



def tester():
	solved = 	[
				[4,3,5,2,6,9,7,8,1],
				[6,8,2,5,7,1,4,9,3],
				[1,9,7,8,3,4,5,6,2],
				[8,2,6,1,9,5,3,4,7],
				[3,7,4,6,8,2,9,1,5],
				[9,5,1,7,4,3,6,2,8],
				[5,1,9,3,2,6,8,7,4],
				[2,4,8,9,5,7,1,3,6],
				[7,6,3,4,1,8,2,5,9]
				]

	for i in range(0,9):
		for j in range(0,9):
			check = valid(solved, solved[i][j], i, j)
			if check == False:
				print(f"Not valid")
				exit()
	print(f"Valid")


if __name__ == '__main__':
	main()