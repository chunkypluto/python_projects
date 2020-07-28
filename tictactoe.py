#! /usr/bin/python
# -*- coding: utf=8 -*-

from IPython.display import clear_output
import random

def display_board(board):
	
	clear_output()
	print('-'*13)
	print(f'| {board[7]} | {board[8]} | {board[9]} |')
	print('-'*13)
	print(f'| {board[4]} | {board[5]} | {board[6]} |')
	print('-'*13)
	print(f'| {board[1]} | {board[2]} | {board[3]} |')
	print('-'*13)


def player_input():
	
	# ask for user input, x or o
	marker=''
	# keep asking for input if it's not X and not O
	while marker!='X' and marker!='O':
		marker = input('Player 1 please enter X or O: ').upper()
	# assign value for each player based on input
	if marker == 'X':
		return ('X','O')
	else:
		return ('O','X')
	# return a tuple (player1marker, player2marker)

def place_marker(board, marker, position):
	
	board[position]=marker
	return board

def win_check(board, mark):
#     print([a for a in range(len(board)) if board[a]==mark])
	# win conditions: rows, cols, and diags
	# return true if won 
	return board[1]==board[2]==board[3]==mark or \
	board[4]==board[5]==board[6]==mark or \
	board[7]==board[8]==board[9]==mark or \
	board[1]==board[4]==board[7]==mark or \
	board[2]==board[5]==board[8]==mark or \
	board[3]==board[6]==board[9]==mark or \
	board[1]==board[5]==board[9]==mark or \
	board[3]==board[5]==board[7]==mark


# print(random.randint(0,1))
def choose_first():
	if random.randint(1,2)==1:
		return 'Player 1 goes first'
	else:
		return 'Player 2 goes first'

def space_check(board, position):
	# return true if the position is empty
	return board[position]==' '


def full_board_check(board):
	# return true if no empty position in 1-9
	return ' ' not in board[1:]

def player_choice(board):
	# ask for player position 1-9
	# use space_check() to check for free space
	# return position for later use in place_marker()
	# infinite loop if the board is already full; 
	# but won't be necessary if using the full_board_check in the main function
	i=0
	while i<5:
		try:
			pos = int(input('Enter a position (1-9): '))
			if space_check(board,pos) and pos>0:
				return pos
			else:
				print('Position not available')
		except:
			print('Please enter an integer (1-9)')
		i+=1
	print('Max tries attempted. Game over.')


def replay():
	
	return input('Play again? y/n: ').lower()=='y'

print('Welcome to Tic Tac Toe!')

# main function
while True:
	# Set the game up here
	board = [' ']*10
	# ask for player input
	(p1marker,p2marker) = player_input()
	# decide on who's turn firs
	turn = choose_first()
	print(turn)
	action = input('Ready to play? y/n: ')
	game_on = False
	if action =='y':
		game_on=True
	while game_on:
		display_board(board)
		#Player 1 Turn
		if turn == 'Player 1 goes first':
			print(f'Player 1 {p1marker}')
			# ask player for position
			pos = player_choice(board)
			# place position on the board
			board = place_marker(board,p1marker,pos)
			# check if win or tie
			if win_check(board,p1marker):
				display_board(board)
				print('Player 1 has won the game. Congrats!')
				game_on = False
			elif full_board_check(board):
				display_board(board)
				print('No more positions available. Tie Game!')
				game_on = False
			else:
#                 display_board(board)
				turn = 'Player 2 goes first'
		# Player2's turn.
		else:
			print(f'Player 2 {p2marker}')
			# ask player for position
			pos = player_choice(board)
			# place position on the board
			board = place_marker(board,p2marker,pos)
			# check if win or tie
			if win_check(board,p2marker):
				display_board(board)
				print('Player 2 has won the game. Congrats!')
				game_on = False
			elif full_board_check(board):
				display_board(board)
				print('No more positions available. Tie Game!')
				game_on = False
			else:
#                 display_board(board)
				turn = 'Player 1 goes first'

	if not replay():
		break
