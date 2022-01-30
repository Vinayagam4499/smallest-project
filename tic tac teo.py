#This one for making the boards
board = ['-' for i in range(9)]


#this one printing the boards orderly
def BoardDisplay():
    print('|',board[0], '|', board[1], '|', board[2],'|')
    print('|',board[3], '|', board[4], '|', board[5],'|')
    print('|',board[6], '|', board[7], '|', board[8],'|')

#Create the Players
player_1 = "X"
player_2 = "O"

#This will be the possible movement for the player to reach winning the game
def check_conditions(player):
    conditions = [
    [0,1,2],[3,4,5],[6,7,8],[0,3,6],
    [1,4,7],[2,5,8],[0,4,8],[2,4,6],
]
#The loop will be checking the condtions
    for check in conditions:
        if board[check[0]] == player and board[check[1]] == player and board[check[2]] == player:
            return 1
    #for loop using else statement
    else:
        return 0

#Create the function to start the game
def start_game():
    BoardDisplay()
    while True:
        #This one extra while loop was used to humping the player 2
        while True:
            #enter the player position
            player1_option = input(f"{player_1}, Enter Your Position: ")
            
            #This was used only 1-9 integer numbers only allowed
            if player1_option not in[str(i) for i in range(10)]:
                print("Please Enter [1-9]")
                #then using continue jump the next conditon
                continue
            #the board positions are in '-' so this player
            if board[int(player1_option)-1] == "-":
                board[int(player1_option)-1] = player_1
                #to pass the function to BoardDisplay()
                BoardDisplay()
                #again attach the functions to player win of lose
                if check_conditions(player_1):
                    return (f'Winner : {player_1}')
                break
            else:
                print("This place is not empty")
        #the will be all 9 boxes are fill the game will bre return and ask you want to play again?
        if len([i for i in board if i == '-']) == 0:
            return ''

        #above all the same
        while True:
            player2_option = input(f"{player_2}, Enter Your Postion: ")
            
            if player2_option not in [str(i) for i in range(9)]:
                print("Please Enter [1-9]")
                continue
            
            if board[int(player2_option)-1] == "-":
                board[int(player2_option)-1] = player_2
                BoardDisplay()
                if check_conditions(player_2):
                    return (f'Winner :{player_2}')
                break
            else:
                print("This place is not empty")


#printing the condition
print(start_game())

#this will loop over fresh new board start the game again.
while True:
    play_again = input("Do you want to Play Again [y/n]: ")
    if play_again in "yY"-:
        board = ['-' for i in range(9)]
        print(start_game())
    else:
        exit()