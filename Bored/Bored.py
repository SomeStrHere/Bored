# Console program that will return from a list; a random chore, a random fun thing to do, or a 
# random selection from a list of both chores and fun things to do.
#
# V: 0.1.1

import sys
import random
from Helpers import * # Source of clearConsole()

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


def generateActivity() :
    
    chores = ['Washing Up', 'Laundry']
    fun = ['Watch TV', 'Play a game']

    allActivities = chores + fun
    print(allActivities)

    if menu() == 'R' :
        displayOutput(random.choice(allActivities))
    elif menu() == 'C' :
        displayOutput(random.choice(chores))
    elif menu() == 'F' :
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
