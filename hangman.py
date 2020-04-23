import random


def hide(string):
    tmp = ""
    for i in range(len(string)):
        tmp += "-"
    return tmp


def change_letter(letter, string, hidden_string):
    help_string = ""
    for i in range(len(string)):
        if letter == string[i]:
            help_string += letter
        else:
            help_string += hidden_word[i]
    return help_string


print("H A N G M A N")

flag = True

while flag:
    choose = input('Type "play" to play the game, "exit" to quit: ')
    if choose == "play":
        word_list = ['python', 'java', 'kotlin', 'javascript']
        random_word = random.choice(word_list)
        hidden_word = hide(random_word)
        letter = []
        i = 8

        while i > 0:
            print("\n" + hidden_word)
            letter.append(input("Input a letter: "))
            if 1 != len(letter[-1]):
                print("You should print a single letter")
            elif letter.count(letter[-1]) > 1:
                print("You already typed this letter")
            elif (97 > ord(letter[-1])) or (ord(letter[-1]) > 122):
                print("It is not an ASCII lowercase letter")
            else:
                if letter[-1] in random_word:
                    if letter[-1] in hidden_word:
                        i -= 1
                        print("No improvements")
                        if 0 == i:
                            print("You are hanged!")
                    else:
                        hidden_word = change_letter(letter[-1], random_word, hidden_word)
                        if hidden_word in random_word:
                            i = 0
                            print("You guessed the word!")
                            print("You survived!")
                else:
                    i -= 1
                    print("No such letter in the word")
                    if 0 == i:
                        print("You are hanged!")
    elif choose == "exit":
        flag = False
