import random 


def load_file():

    with open('words.txt') as file:
        contents = file.read()
        # Get a Random Word
        word = list(map(str,contents.split()))
        # return word
        random_word = random.choice(word)
        return random_word
        # no_of_letter = len(random_word)

def select_word():
    get_word = load_file()
    return get_word


def Player_name():
    Player_name = input('Enter your Name: ')
    return Player_name

def Menu():
    menus = input("Type to Start Game'Play' or 'Exit' to quit: ")
    if menus == "play" or "Play":
        print('Loading...')
    elif menus == "Exit":
        print('Quit.')
        exit()
    else:
        print('Invaild Input')
        Menu()

def game_control():

        user = Player_name()

        print(f"Welcome {user},Let's Start the Game")
        print("You Have 3 Guesses to fill the word")
        print("Let's Go.....")

        play_game = Menu()
        play_game
        # return user

        # get word
        word = select_word()
        no_of_letters = len(word)
        no_of_Guesses = 7


        dash = "_" * no_of_letters
        print(f"{dash}", end = "")
        print("\n")




        while no_of_Guesses > 0:
                user_guess =  input("Enter your guess: ")
                # 1 character at 1 time
                if len(user_guess) > 1:
                    print("You can only guess one letter at a time")
                    continue
                # when the guess is correct then print correct
                if user_guess in word:
                    print("Correct Guess")
                # Update the dash variable to correct guesses
                for i in range(no_of_letters):
                    if word[i] == user_guess:
                        dash = dash[:i] + user_guess + dash[i+1:]
                        print(dash, end = "")
                # if all guesses are = to word then you Won the game    
                if dash == word:
                    print(f"{user} - Won - word: {word}")
                    break
                # when wrong guess decrease 1 from guess
                if user_guess not in word:
                    no_of_Guesses -=1
                    print("Wrong Guess")
                    print("You have", no_of_Guesses, "guesses left")
                    # when the guess equal to 0 then you lost the game
                if no_of_Guesses == 0:
                    print(f"{user} - Lost - word: hangman")
                # create hangman with print
                    print( """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    """)
                    
        print("You have", no_of_Guesses, "guesses left")

        print("The word was", word)

game_control()

# Using while to continue game after game finished!
while True:
    play_again = input("Do you want to Play Again 'yes' or 'no' ")
    if play_again == "yes":
        game_control()
    elif play_again == "no":
        print('Thanks for Playing')
        break    




