'''
def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(1) and l[0] != 0:
            return True
        else:
            return False

        for row in game:
            print(row)
            if all_same(row):
                print(f"Player {row[0]} is the winner horizontally!")
                return True

     '''  

game = [[1,2,3],
        [4,5,6],
        [7,8,0]]

def win(game):
    for row in game:
        for i in range(len(row)):
            print(row[i])
win(game)
'''
def win(current_game):
    for row in game:
        print(row)
        col1 = row[0]
        print(col1)
        col2 =row[1]
        print(col2)
        col3 = row[2]
        print(col3)
        if col1 ==col2==col3:
            print("winner")
win(game)'''
