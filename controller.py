# Password-Generator 
# controller.py
# Created by Mauro J. Pappaterra on 06 of November 2017.

import time
from pathlib import Path

# GLOBAL VARIABLES
dictionary = []
use_default = True

custom_dictionary = "" # dictionaries/idiot.txt

# MAIN PROGRAM METHOD / START SCREEN
def start(m,v):

    exit = False
    while (not exit):

        print(v.welcome)
        print(v.instructions)

        read = input().lower()

        while (read != 's' and read != 'q'):
            print (v.error_start)
            read = input().lower()

        if (read == 's'):
            exit = main(m,v)

        if (read == 'q'):
            exit = True
    print (v.exit)

# MAIN MENU
def main (m,v):
    print(v.menu)

    read = input().lower()
    while (read != 'c' and read != 'd' and read != 'a' and read != 'q'):
        print (v.error_input)
        read = input().lower()

    if (read == 'c'):
         return password(m,v)
    elif (read == 'd'):
        return dictionary_menu(m,v)
    elif (read == 'a'):
        return about(m,v)
    elif (read == 'q'):
        return True

# ABOUT PAGE
def about(m,v):

    print (v.about)

    read = input().lower()
    while (read != 'b' and read != 'q'):
        print (v.error_input)
        read = input().lower()

    if (read == 'b'):
        return main(m,v)
    elif (read == 'q'):
        return True

# CREATE A NEW PASSWORD MENU
def password(m,v):
    global dictionary

    if (use_default):
        dictionary = m.createDictionary("dictionaries/dictionary_simple.txt")[:]

    size = len(dictionary)

    print (v.number_words)
    no_words = input()
    while (not (no_words.isdigit()) or not(1 <= int(no_words) <= 9999)):
        print(v.error_words)
        no_words = input()

    no_words = int (no_words)
    entropy = m.getEntropy(size, no_words)

    print (v.info_dictionary(size, no_words) + str(entropy) + " bits of entropy")
    time.sleep(1)
    print (v.your_password + m.getPassword(dictionary, no_words))

    ten = m.estimateLength(10, entropy)
    twenty_six = m.estimateLength(26, entropy)
    fifty_two = m.estimateLength(52, entropy)
    sixty_two = m.estimateLength(62, entropy)

    time.sleep(1)

    v.compare(ten, twenty_six, fifty_two, sixty_two)

    print (v.password_menu)

    read = input().lower()
    while (read != 'b' and read != 'n' and read != 'g' and read != 'd' and read != 'q'):
        print (v.error_input)
        read = input().lower()

    if (read == 'b'):
        return main(m,v)
    elif (read == 'g'):
        return generate_new(m, v, dictionary, no_words)
    elif (read == 'n'):
        return password(m,v)
    elif (read == 'd'):
        return dictionary_menu(m,v)
    elif (read == 'q'):
        return True

# GENERATE PASSWORD MENU
def generate_new(m, v, dictionary, no_words):

    print (v.your_password + m.getPassword(dictionary, no_words))
    print(v.password_menu)

    read = input().lower()
    while (read != 'b' and read != 'n' and read != 'g' and read != 'd' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == 'b'):
        return main(m,v)
    elif (read == 'g'):
        return generate_new(m, v, dictionary, no_words)
    elif (read == 'n'):
        return password(m,v)
    elif (read == 'd'):
        return dictionary_menu(m,v)
    elif (read == 'q'):
        return True

# DICTIONARY MENU
def dictionary_menu (m,v):
    global use_default
    global dictionary
    global custom_dictionary

    print (v.dictionary)

    read = input().lower()
    while (read != 's' and read != 'f'and read != 'p'and read != 'b' and read != 'c' and read != 'q'):
        print (v.error_input)
        read = input().lower()

    if (read == 's'):
        use_default = True
        print (v.simple)
        return dictionary_menu(m,v)

    elif (read == 'f'):
        use_default = False
        dictionary = m.createDictionary("dictionaries/dictionary_full.txt")[:]
        print(v.full)

        return dictionary_menu(m,v)

    elif (read == 'p'):

        print (v.ask_path)
        read = input().lower()
        custom_dictionary = Path(read)

        while (not custom_dictionary.is_file()):

            if (read == 'c' or read == 'b'):
                custom_dictionary = ""
                return dictionary_menu(m, v)

            print(v.error_path)
            read = input().lower()
            custom_dictionary = Path(read)

        print(v.path + read + ")")
        print(v.custom)
        use_default = False
        dictionary = m.createExternal(custom_dictionary)[:]

        return dictionary_menu(m,v)

    elif (read == 'b'):
        return main(m,v)

    elif (read == 'c'):
        return password(m,v)

    elif (read == 'q'):
        return True