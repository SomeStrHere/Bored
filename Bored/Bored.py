# Console program that will return from a list; a random chore, a random fun thing to do, or a 
# random selection from a list of both chores and fun things to do.
#
# V: 0.1.1

import sys
import random
from Helpers import * # Source of clearConsole()
import os # Used in testing 


def menu():

    print('Bored\n')
       
    print('R - Displays a random fun or chore activity')
    print('C - Displays a random chore activity')
    print('F - Displays a random fun activity')
    print('X - Exits program')
    print('\nPlease enter option :')

    userChoice = input('\n').upper()

    validOptions = {'R', 'C', 'F', 'X'} 
    valid = userChoice in (validOptions)

    if valid == False :
        clearConsole(0)
        print('Not a valid option, please try again\n')
        menu()

    elif userChoice == 'X' :
            sys.exit()
    else :
        return(userChoice)

def readFile(list) : 

    print(os.getcwd())

    READ = 'r'
    fileName = list + '.txt'

    with open(fileName, READ) as f :
        # Reads the entire file
        dictionary = f.readlines() 

    # Seperates each word to create a list of words
    Activitylist = [word.strip() for word in dictionary] 
        
    return(ActivityList) 


def generateActivity() :
    
    chores = ['Washing Up', 'Laundry']
    fun = ['Watch TV', 'Play a game']

    allActivities = chores + fun
    print(allActivities)

    if menu() == 'R' :

        try :
           allList = readFile('all')
           displayOutput(random.choice(allList))
           # TODO enhancement = derive all list from combing chore.txt and fun.txt

        except FileNotFoundError :
            print('Sorry, all activities list, file not found')
            print('Using default all activities list...\n')
            displayOutput(random.choice(allActivities))

        except :
            print('Sorry there was an error with all.txt')
            print('Using default all activities list...\n')
            displayOutput(random.choice(allActivities))

    elif menu() == 'C' :

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

    elif menu() == 'F' :
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
        generateActivity()


      
def displayOutput(activity) :
    print(activity)
     

def main() : 
    
    generateActivity()


if __name__ == "__main__" :
    main()
