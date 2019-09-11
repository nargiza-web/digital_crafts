game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def game_board(game_map, player = 0, row = 0, column = 0, just_display=False):
    try:
        if game_map[row][column] != 0 :
            print("Occupied!choose another")
        print('   0  1  2')
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("input 0, 1 or 2 only",e)
        return False

def winner(current_game):
    three_in_a_row = [[game[0][0],game[0][1],game[0][2]],
                       [game[1][0],game[1][1],game[1][2]],
                       [game[2][0],game[2][1],game[2][2]],
                       [game[0][0],game[1][0],game[2][0]],
                       [game[0][1],game[1][1],game[2][1]],
                       [game[0][2], game[1][2],game[2][2]],
                       [game[0][0],game[1][1],game[2][2]],
                       [game[2][0],game[1][1],game[0][2]]]
    for row in three_in_a_row:
        if row[0]==row[1]==row[2] and row[0]==row[1]==row[2] !=0:
            print('winner!')
            exit()
    return False
  
def take_turn(current_player):
    if current_player == 'X':
        return  'Y'
    elif current_player == 'Y':
        return 'X'    
    #print(f"{current_player}'s turn'")
    #return current_player

player = 'X'
while True:
    game_map = game
    row = int(input('enter row? '))
    column = int(input('enter column? '))
    
    game_board(game_map, player,row,column)

    player=take_turn(player)
    winner(player)

   
    
    