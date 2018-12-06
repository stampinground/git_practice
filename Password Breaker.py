""" Create a program which stores a random password which can be guessed
or bruteforced"""

from random import randint

password = str(randint(0,9999))

print ()
print ("Welcome SHITTY password breaker. Enter 'q' to quit or 'b' to bruteforce.")
print ()

def init():
    access = False
    while access == False:
        guess = input("Please enter your 4-digit PIN number: ")
        pass_guess(str(guess))
        if guess == "q" or guess == password:
            break

def pass_guess(guess):
    if guess == password:
        print ("Access granted")
    elif guess == "q":
        print ("Quitting...")
    elif guess == "b":
        pass_break()
    else:
        print ("Incorrect password, please try again")

def pass_break():
    count = 0
    while count < 10000:
        pass_guess(str(count))
        count += 1
        print("Trying", count)
        if count == int(password):
            print ("Access granted!")
            break

init()
