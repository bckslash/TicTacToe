import random, os

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

board = [' ' for x in range(10)]

def instert_letter(letter, pos):
	board[pos] = letter

def is_pos_blank(pos):
	return board[pos] == ' '

def print_board(board):
	print('+-------+-------+-------+')

	print('|       |       |       |')
	print(f'|   {board[1]}   |   {board[2]}   |   {board[3]}   |')
	print('|       |       |       |')

	print('+-------+-------+-------+')

	print('|       |       |       |')
	print(f'|   {board[4]}   |   {board[5]}   |   {board[6]}   |')
	print('|       |       |       |')

	print('+-------+-------+-------+')

	print('|       |       |       |')
	print(f'|   {board[7]}   |   {board[8]}   |   {board[9]}   |')
	print('|       |       |       |')

	print('+-------+-------+-------+')

def is_winner(board, mark):
	return ((board[1] == mark and board[2] == mark and board[3] == mark) or
		(board[4] == mark and board[5] == mark and board[6] == mark) or 
		(board[7] == mark and board[8] == mark and board[9] == mark) or
		(board[1] == mark and board[4] == mark and board[7] == mark) or 
		(board[2] == mark and board[5] == mark and board[8] == mark) or 
		(board[3] == mark and board[6] == mark and board[9] == mark) or
		(board[1] == mark and board[2] == mark and board[3] == mark) or
		(board[1] == mark and board[5] == mark and board[9] == mark) or
		(board[3] == mark and board[5] == mark and board[7] == mark))

def player_move():
	run = True

	while run:
		move = input("Enter position (1-9): ")
		try:
			move = int(move)
			if move > 0 and move < 10:
				if is_pos_blank(move):
					run = False
					instert_letter('X', move)
				else:
					print("Position is full!")
			else:
				print("Enter valid number!")
		except:
			print("Type the number")

def computer_move():
	possible_moves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0]

	move = 0

	open_corners = []
	for i in possible_moves:
		if i in [1, 3, 7, 9]:
			open_corners.append(i)

	open_edges = []
	for i in possible_moves:
		if i in [2, 4, 6, 8]:
			open_edges.append(i)

	for let in ['X', 'O']:

		for i in possible_moves:

			board_copy = board[:]
			board_copy[i] = let

			if is_winner(board_copy, let):
				move = i
				return move

	if 5 in possible_moves:
		move = 5 
		return move

	if len(open_corners) > 0:
		move = random.choice(open_corners)

	if len(open_edges) > 0:
		move = random.choice(open_edges)

	return move

def is_board_full(board):
	return board.count(' ') < 1

def main():
	print("-------------------------")
	print(" WELCOME TO Tic-Tac-Toe!")
	print('-------------------------\n')
	print_board(board)

	while not (is_board_full(board)):

		if not (is_winner(board, 'O')):
			player_move()
		else:
			print_board(board)
			print("Computer Wins")
			break

		if not (is_winner(board, 'X')):
			move = computer_move()
			if move == 0:
				print_board(board)
				print("Tie Game")
				break
			else:
				instert_letter('O', move)
				print('Computer placed O in {}!\n'.format(move))
				print_board(board)
		else:
			print_board(board)
			print("Player Wins")
			break
		
	if is_board_full(board):
		print_board(board)
		print("Tie Game")


if __name__ == '__main__':

	clear()
	while True:
		answer = input("Do you want to play? [Y/n]: ")
		clear()
		if answer.lower() == 'y' or answer.lower() == 'yes':
			board = [' ' for x in range(10)]
			main()
		else:
			print("-------------------------")
			print("   Thanks' for playing")
			print("-------------------------")
			break
