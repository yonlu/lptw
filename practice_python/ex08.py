isPlaying = True
while (isPlaying):
    print("This is the JoKenPo Game!")
    print("When it's your turn, type either 'rock', 'paper' or 'scissors'")
    player1 = input("Player one: ")
    player2 = input("Player two: ")

    if player1 == player2:
        print("It's a tie!")
    elif player1 == 'rock':
        if player2 == 'scissors':
            print("Player One wins!")
        else:
            print("Player Two wins!")
    elif player1 == 'scissors':
        if player2 == 'paper':
            print("Player One wins!")
        else:
            print("Player Two wins!")
    elif player1 == 'paper':
        if player2 == 'rock':
            print("Player One wins!")
        else:
            print("Player Two wins!")
    else:
        print("Invalid input! You have not entered rock, paper or scissors, try again!")

    quitPlaying = input("Do you want to quit playing? (yes/no): ")

    if quitPlaying == "yes":
        isPlaying = False

