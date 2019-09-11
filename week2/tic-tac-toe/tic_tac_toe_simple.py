import data
import view

# deciding for winner

def check_if_i_won(current_player):
    three_in_a_rows = [[data.board[0][0], data.board[0][1], data.board[0][2]],
                       [data.board[1][0], data.board[1][1], data.board[1][2]],
                       [data.board[0][0], data.board[1][0], data.board[2][0]],
                       [data.board[0][1], data.board[1][1], data.board[2][1]],
                       [data.board[0][2], data.board[1][2], data.board[2][2]],
                       [data.board[2][0], data.board[2][1], data.board[2][2]],
                       [data.board[0][0], data.board[1][1], data.board[2][2]],
                       [data.board[2][0], data.board[1][1], data.board[0][2]]]
    
    for row in three_in_a_rows:
        if row[0]==row[1]== row[2]:
            return True
    return False

def place_position(position, current_player):
    x = data.positions[position][0]
    y = data.positions[position][1]
    data.board[x][y] = current_player

def take_turn(current_player):
    place_position(input('Choose your position[1-9]: '), current_player)

def switch_players(current_player):
    if current_player == 'X':
        return 'O'
    elif current_player == 'O':
        return 'X'

def play_game():
     current_player = 'X'
     view.board(current_player)
     winner = ''
     while winner == "":
         take_turn(current_player)
         if check_if_i_won(current_player):
             winner = current_player
             print(f'Player {winner} won!')
             return
         current_player = switch_players(current_player)
         view.board(current_player)

play_game()