print('Position must be in format separated by space.')
board = [['_','_','_'],['_','_','_'],['_','_','_']]  # makes a 3*3 board
from random import randint  # for bot selection
# We write a function that takes a the current board status and makes decision
def win_condition(status):
	players = {'X':'User', 'O': 'Computer'}
	for j in players:
		if status[1][1] == status[2][2] == status[0][0] == j or status[0][2] == status[1][1] == status[2][0] == j:
			return players[j] + ' wins'
		for i in range(3):
			if status[i][0] == status[i][1] == status[i][2] == j:
				return players[j] + ' wins'
			elif status[0][i] == status[1][i] == status[2][i] == j:
				return players[j] + ' wins'
	if '_' not in status[0] and '_' not in status[1] and '_' not in status[2]:
		return 'Draw'
	return None
# Player and computer make moves here
for i in range(9):
# Player makes moves
	while True:
		player = input('Enter the position of your play:')
		if board[int(player[0]) - 1][int(player[2]) - 1] == '_':
			board[int(player[0]) - 1][int(player[2]) - 1] = 'X'
			break
		else: # Player cannot take already occupied position
			print('Please choose another position')
			continue
# Prints board status
	print('''{} {} {}
{} {} {}
{} {} {}'''.format(board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2]))
# Win condition
	if win_condition(board) != None:
		print(win_condition(board))
		quit()
# Computer makes moves
	while True:
		bot_row = randint(1,3)
		bot_col = randint(1,3)
		if board[bot_row - 1][bot_col - 1] == '_':
			print('Bot chooses {} {}'.format(bot_row, bot_col))
			board[bot_row - 1][bot_col - 1] = 'O'
			break
		else:
			continue
# Prints board status
	print('''{} {} {}
{} {} {}
{} {} {}'''.format(board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2]))
# Win Condition
	if win_condition(board) != None:
		print(win_condition(board))
		quit()
	else:
		continue