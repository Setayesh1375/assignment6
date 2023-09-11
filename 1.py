import pyfiglet
import random


def show():
    for row in game_board:
        for cell in row:
            print (cell , end=" ")
        print()

def check_game():
    if (game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X")or(game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X")or(game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X")or(game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X")or(game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X")or(game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X")or(game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X")or(game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X"):
        print ("player 1 wins")
    if (game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O")or(game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O")or(game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O")or(game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O")or(game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O")or(game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O")or(game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O")or(game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O"):
        print ("player 2 wins")
    

title = pyfiglet.figlet_format("Tic Tac Toe" , font= "slant")
print (title)

print (" Please enter game :")
mode = int(input( "1) One Player:  \n 2) Two Players: \n"))

game_board =["-","-","-"
             "-","-","-"
             "-","-","-"]
show()
while True:

    if mode == 1:
        print ("player")
        while(True):

                row = int(input("row: "))
                col = int (input("col: "))
                if 0<= row <=2 and 0<= col <=2 :
                    if game_board[row][col] == "-":
                        game_board[row][col] = "O"
                        break
                    else:
                        print("jer nazan :/")
                else:
                    print(" mesle adam vared kon ")
                show()
                player = "Player"
                check_game()

        print ("CPU")
        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)
            if game_board [row][col] == "_":
                game_board [row][col] = "O"
                break
        
        show()
        player = "CPU"
        check_game()

    elif mode == 2:
            print ("Player 1")
            while(True):

                row = int(input("row: "))
                col = int (input("col: "))
                if 0<= row <=2 and 0<= col <=2 :
                    if game_board[row][col] == "-":
                        game_board[row][col] = "X"
                        break
                    else:
                        print("jer nazan :/") 
                else:
                    print(" mesle adam vared kon ")        
                show()
                player = "Player 1"
                check_game()
    print ("Player 2")
    while True:
            row = int (input("row: "))
            col = int (input("col: "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                        if game_board [row][col] == "_":
                            game_board [row][col] = "O"
                            break
                        else:
                            print ("This cell is filled.")
            else:
                print ("The input number must be between 0 and 2.")
                
            show()
            player = "Player 2"
            check_game()
    else:
         while mode != 1 or 2:
            print ("Select between 1 and 2.")
            mode = int(input("1) One Player:  \n2) Two Players: \n"))
            break        