# Console program that will return from a list; a random chore, a random fun thing to do, or a 
# random selection from a list of both chores and fun things to do.
#
# V: 0.2.0

import sys
import random
from clearConsole import *

def menu():

    print('Bored\n')
       
    print('A - Displays a random fun or chore activity')
    print('C - Displays a random chore activity')
    print('F - Displays a random fun activity')
    print('X - Exits program')
    print('\nPlease enter option :')

    userChoice = input('\n').upper()

    if userChoice == 'X' :
        clearConsole(0)
        sys.exit

    elif userChoice == 'A' :
        generateActivity('all')

    elif userChoice == 'C' :
        generateActivity('chore')

    elif userChoice == 'F' :
        generateActivity('fun')

    else :
        print('Invalid option, please try again')
        menu()


def generateActivity(userChoice) :
    
    #Default lists
    chores = ['Wash Dishes', 'Do Laundry', 'Clean Bathroom', 'Walk The Dog', 'Hoover/Sweet Floors']
    fun = ['Watch TV', 'Play a game', 'Have a run', 'Go Swimming', 'Draw/Paint']

    allActivities = chores + fun

    if userChoice == 'all' :

        try :
           allList = readFile('all')
           displayOutput(random.choice(allList))

        except FileNotFoundError :
            print('Sorry, all activities list, file not found')
            print('Using default all activities list...\n')
            displayOutput(random.choice(allActivities))

        except :
            print('Sorry there was an error with all.txt')
            print('Using default all activities list...\n')
            displayOutput(random.choice(allActivities))
            

    elif userChoice == 'chore' :

        try :
            choreList = readFile('chore')
            displayOutput(random.choice(choreList))

        except FileNotFoundError :
            print('Sorry, chore activities list, file not found ')
            print('Using default all activities list...\n')
            displayOutput(random.choice(allActivities))

        except :
            print('Sorry there was an error with chore.txt')
            print('Using default chore list...\n')
            displayOutput(random.choice(chores))

    elif userChoice == 'fun' :
        try :
            funList = readFile('fun')
            displayOutput(random.choice(funList))

        except FileNotFound :
            print('Sorry, fun activities, list, file not found')
            print('Using default fun activities list...\n')
            displayOutput(random.choice(fun))

        except :
            print('Sorry there was an error with fun.txt')
            print('Using default fun activities list...\n')
            displayOutput(random.choice(fun))
    else :
        print('Sorry, there was an error')
        menu()


def readFile(list) : 

    READ = 'r'
    fileName = list + '.txt'

    if list == 'all' : 

        with open('fun.txt', READ) as f :
            dictionary_fun = f.readlines() 

            funList = [word.strip() for word in dictionary_fun]

        with open('chore.txt', READ) as c :
            # Reads the entire file
            dictionary_chore = c.readlines() 

            choreList = [word.strip() for word in dictionary_chore] 

        ActivityList = funList
        ActivityList.extend(choreList)

    else :

        with open(fileName, READ) as f :
            # Reads the entire file
            dictionary = f.readlines() 

        # Seperates each word to create a list of words
        ActivityList = [word.strip() for word in dictionary] 
     
    return(ActivityList)

     
def displayOutput(activity) :
    
    clearConsole(0)
    print('\nYour randomly selected activity is:\n')
    print(activity)
     

def main() : 
    
    menu()


if __name__ == "__main__" :
    main()
