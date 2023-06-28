"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jakub Havel
email: havel8jakub@seznam.cz
discord: Kuba H.#6482
"""
import random
def number_cow(hidden, in_number):
    '''
    Determines the occurrence of a number.
    '''
    cow_numbers=[x for x in in_number if x in hidden]
    cow=len(cow_numbers)
    return cow
def number_bull(hidden, in_number):
    '''
    Determines the position of a number.
    '''
    bull_numbers = [x for x, y in zip(hidden, in_number) if x == y]
    bull = len(bull_numbers)
    return bull
def print_bull(bull):
    '''
    Determines singular or plural form for bull.
    '''
    if bull == 1:
        return "bull {}".format(bull)
    else:
        return "bulls {}".format(bull)
def alignment(bull,cow):
    '''
    Evaluating cow and bull and outputting singular or plural form for cow.
    '''
    if bull > 0:
        cow -= bull
    if cow == 1:
        return "cow {}".format(cow)
    else:
        return "cows {}".format(cow)
print("Hi there!")
print(30*"-")
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(30*"-")
print("Enter a number:")
print("If you want to end, type 'end' into the input.")
print(30*"-")
while True:
    numbers = list(range(0,10))
    random.shuffle(numbers)
    if numbers[0] == 0:
        play_number = numbers[1:5]
    else:
        play_number = numbers[:4]
    str_number=""
    for nn in play_number:
        str_number+= str(nn)
    print(str_number)
    count = 0
    used_numbers = set()
    while True:
        variable = input(">>> ")
        if variable == "end":
            print("Ending the game.")
            print(30 * "-")
            break
        count += 1
        if not variable.isdigit():
            print("Input is not a digit.")
            print(30 * "-")
            continue
        if len(variable) > 4:
            print("The input is too long.")
            print(30 * "-")
            continue
        if len(variable) < 4:
            print("The input is too short.")
            print(30 * "-")
            continue
        if len(set(variable)) != len(variable):
            print("The digits in the input are repeated.")
            print(30 * "-")
            continue
        if variable[0] == "0":
            print("The input must not start with zero.")
            print(30 * "-")
            continue
        clear_bull = (print_bull(number_bull(str_number, variable)))
        clear_cow = (alignment(number_bull(str_number,variable), number_cow(str_number, variable)))
        if variable == str_number:
            break
        print("{}, {}".format(clear_bull, clear_cow))
    print("ACorrect, you've guessed the right numberin %d guesses!" %(count))
    if count <= 3:
        print("That' s amazing.")
        pass
    elif count <=10:
        print("That' s avarage.")
        pass
    elif count <=16:
        print("That' s not so goog.")
        pass
    else:
        print("That' s terrible.")
    print(30 * "-")
    again = input("Do you want to play again? yes/no:")
    if again == "yes":
        continue
    else:
        break

