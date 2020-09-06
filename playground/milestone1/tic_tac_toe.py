# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 23:13:58 2020

@author: lohit
"""
def display_board(board):
        print('\n'*100)
        print('     |     |     ')
        print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
        print('     |     |     ')
        print('-----------------')
        print('     |     |     ')
        print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
        print('     |     |     ')
        print('-----------------')
        print('     |     |     ')
        print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
        print('     |     |     ')
        
def player_input():
    
    marker='wrong'
    while marker !='X' and marker !='O':

        marker=input('player1: do you want to be X or O:').upper()
    
    player1=marker
    
    if player1=='X':
        player2='O'
        return(player1,player2)
    else:
        player2='X'
        return(player1,player2)
    
def place_marker(board, marker, position):
    board[position]=marker.upper()

def win_check(board, mark):
    return((board[7]==board[8]==board[9]== mark) or
           (board[4]==board[5]==board[6]== mark) or
           (board[1]==board[2]==board[3]== mark) or
           (board[7]==board[4]==board[1]== mark) or
           (board[8]==board[5]==board[2]== mark) or
           (board[9]==board[6]==board[3]== mark) or
           (board[7]==board[5]==board[3]== mark) or
           (board[1]==board[5]==board[9]== mark))
          
import random as ran

def choose_first():
    
    if ran.randint(0,1)==0:
        return('Player 1')
    else:
        return('Player 2')

def space_check(board, position):
    return(board[position]==' ')

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return(False)
    return(True)
        
def player_choice(board):
    
    position=0
    
    while position not in range(1,10) or not space_check(board,position):
        
        position=int(input('enter the next position (1-9):'))
        
    return(position)

def replay():
    
    replay_choice='wrong'
    
    while replay_choice !='Y' and replay_choice!='N':
        
        replay_choice=input('do you want to continue: Y or N').upper()
        
    return(replay_choice=='Y')

print('Welcome to Tic Tac Toe!')

while True:
    board=[' ']*10
    
    player1_marker, player2_marker = player_input()
    
    turn= choose_first()
    
    print(f'{turn} will play first')
    
    play_game=input('Ready to play ? y on n')
    
    if play_game.lower()== 'y':
        game_on= True
    else:
        game_on= False
        
    while game_on:
        
        if turn== 'Player 1':
            # display board
            display_board(board)
            # choose a position
            position= player_choice(board)
            place_marker(board,player1_marker,position)
            
           
            # check if they won
            if win_check(board,player1_marker):
                display_board(board)
                print('congratulations! you have won the game')
                break
                
            # check if tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print('the game is drawn!')
                    break
                else:
                    turn= 'Player 2'
            #no tie and no win ? next player turn
        else:    
            display_board(board)
                
            position=player_choice(board)
                
            place_marker(board,player2_marker,position)
                
            if win_check(board,player2_marker):
                display_board(board)
                print('Player 2 has won')
                break
            
            else:
                if full_board_check(board):
                    display_board(board)
                    print('the game is drwan!')
                    break
                else:
                    turn= 'Player 1'


    if not replay():
        break
   