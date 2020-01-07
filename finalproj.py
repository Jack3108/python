from random import randint
import datetime

p1 = False
p2 = False
a = False
p1_total = 0
p2_total = 0
round = 0
writeplayer = ""
writescore = 0

def login(): # Allows both users to login
    global user, player1, player2, p1, p2, file

    if p1 != True: # Determines if player 1 or player 2 is logining in
        print("Hello Player 1, input your username and password to continue.")

    elif p1 == True: # Determines if player 1 or player 2 is logining in
        print("Hello Player 2, input your username and password to continue.")

    f = open("username.txt", "r+") # reads username file and assigns each line to an entry in a list
    usern = f.readlines()
    f.close()
    print(usern)

    user = input("Username: ")
    use = user + "\n"

    for i in range(len(usern)): # checks if username is in list
        if usern[i] == use:
            a = True
            break

    if a == True:
        print("Username Accepted.")

        if p1 == True:
            player2 = user
            if player1 == player2: # if player 1 and player 2 have the same name it adds '(1)' to player 2's name
                player2 += "(1)"

        else:
            player1 = user

        file = user + ".txt"
        try:
            f = open(file, "r")
            pass1 = f.read()
            passw = input("Password: ")
            if passw in pass1 and p1 != True: # Allows player 1 to input password
                p1 = True
                print("Player 1 is logged in.")
                login()
            elif passw in pass1 and p1 == True: # Allows player 2 to input password
                p2 = True
                print("Player 2 is logged in.")
                main()
            else: # If password is wrong restart login
                print("Password Denied.")
                login()

        except FileNotFoundError: # If the username doesn't have a password it allows the user to make one for that username
            newpass()


    else: # If Username
        print("Username Denied.")
        login()

def newpass(): # sets password if username doesnt already have one
    option = input("You dont have a password, would you like to make one (y/n)? ")

    if option == "y":
        f = open(file, "w")
        passwd = input("Input your password: ")
        f.write(passwd) # Write password to user file
        f.close()

        print("Your password has been set.")
    elif option == "n":
        print("No password has been set, exiting program.") # Closes program if no password is set.
        exit()

    else:
        print("Option not valid, only choose either \"y\" or \"n\".") # Reruns code if option is invalid
        newpass()

def main(): # Main menu
    global p1, p2, player1, player2
    print("Options:\n\n 1. Start the game\n 2. Log out\n 3. Quit")
    option = int(input("> "))

    if option == 1:
        game()
    elif option == 2:
        p1 = False
        p2 = False
        player1 = ""
        player2 = ""
        login()
    elif option == 3:
        exit()
    else:
        main()

def game(): # main game
    global round, writeplayer, writescore

    while round < 5:
        roll()
        round += 1

    if p1_total == p2_total:
        print("After {} rounds, {} and {} have the same amount of points, which is {}.".format(rounds + 1, player1, player2,p1_total))
        round += 1
        roll()

    elif p1_total > p2_total:
        print("{} has won, with {} points.".format(player1, p1_total))
        print("{} had {} points.".format(player2, p2_total))
        writeplayer = player1
        writescore = p1_total
        storescore(writeplayer, writescore)

    elif p2_total > p1_total:
        print("{} has won, with {} points.".format(player2, p2_total))
        print("{} had {} points.".format(player1, p1_total))
        writeplayer = player2
        writescore = p2_total
        storescore(writeplayer, writescore)

def roll(): # rolls the die for each player
    global p1_total, p2_total
    print("Round {}".format(round + 1))
    print(player1, "press ENTER to roll your 2 die.")
    input()
    p1_roll1 = randint(1, 6)
    p1_roll2 = randint(1, 6)
    p1_roll = p1_roll1 + p1_roll2
    p1_total += p1_roll
    print("{} you rolled a {} and a {} which equals a {} overall.".format(player1, p1_roll1, p1_roll2, p1_roll))
    print("{} has a total of {}.".format(player1, p1_total))

    print(player2, "press ENTER to roll your 2 die.")
    input()
    p2_roll1 = randint(1, 6)
    p2_roll2 = randint(1, 6)
    p2_roll = p2_roll1 + p2_roll2
    p2_total += p2_roll
    print("{} you rolled a {} and a {} which equals a {} overall.".format(player2, p2_roll1, p2_roll2, p2_roll))
    print("{} has a total of {}.".format(player2, p2_total))

def storescore(player, score):
    try:
        test = open("Scores.txt")
        test.close()

        f = open("Scores.txt", "a+")
        date = datetime.date.today()
        line = "   " + player + "   |   " + score + "   |   " + str(date) + "\n"
        f.write(line)
        f.close()

        f = open("Scores.txt")
        print(f.read())
        f.close()

    except FileNotFoundError:
        f = open("Scores.txt", "a+")
        f.write("   Player   |   Score   |   Date   ")
        f.close()

        storescore(writeplayer, writescore)


login()
