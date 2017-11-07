# Password-Generator 
# view.py.py
# Created by Mauro J. Pappaterra on 06 of 11 2017.

### VIEW

welcome = """                ____                                          __
               / __ \____ ____________      ______  _________/ /
              / /_/ / __ `/ ___/ ___/ | /| / / __ \/ ___/ __  / 
             / ____/ /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /  
            /_/____\\_,_/____/____/ |__/|__/\___\\_/   \__,_/   
              / ____/__  ____  ___  _________ _/ /_____  _____  
             / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/  
            / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /      
            \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     v1.0

              = Create passwords and calculate entropy =                                   

            """
instructions = """Welcome to Password Generator. This short program will help you generate a random password from an
external .txt file and calculate its entropy. You can also compare entropy of different methods! 
Enter 'q' and press <enter> at any time to exit the program.

Enter 's' and press <enter> to begin!
"""

menu = """ Select one of the available options and press <enter>
1 - CREATE PASSWORD => Generate a password and calculate it's entropy!
2 - CHANGE DICTIONARY => Change default dictionary or enter a path to your own text file!
3 - ABOUT => Read more about secure passwords and entropy.

q - quit

"""

about = """ yadda yadda yadda

b - back to menu
q - quit

"""

password_intro = "To create a stronger, but easier to remember password, the program will randomly select words from the selected dictionary."


def entropy(n):
    text = "DICTIONARY: You are using the default dictionary of " + n + " words.\n" + \
           "ENTROPY: The entropy for a 4 word password generated using this dictionary will be of "
    return text


def compare(ten, twentysix, fiftytwo, sixtytwo):
    print("The necessary length for a randomly generated password to have the same entropy, would be:")
    print("From a set of 10 characters [0-9] => " + ten)
    print("From a set of 26 characters [a-z] or [A-Z] => " + twentysix)
    print("From a set of 52 characters [a-z] and [A-Z] => " + fiftytwo)
    print("From a set of 62 characters [a-z] and [A-Z] and [0-9] => " + sixtytwo)

your_password = "--------------------\n" + "Your password is => "

exit = "Exit by user!"
