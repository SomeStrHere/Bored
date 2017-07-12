# Console program that will return from a list; a random chore, a random fun thing to do, or a 
# random selection from a list of both chores and fun things to do.
#
# V: 0.2.0

import sys
import random
from clearConsole import *
#import os # Used in testing 
#import traceback # Used in testing 

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

    if valid :
        if userChoice == 'X' :
            clearConsole(0)
            sys.exit

        else :
            return(userChoice)

    else :
        print('Invalid option, please try again')
        generateActivity()

def readFile(list) : 

    #print(os.getcwd()) # Testing 

    READ = 'r'
    fileName = list + '.txt'

    if list == 'all' : 

        with open('fun.txt', READ) as f :
            # Reads the entire file
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
     
    #print(ActivityList) # Testing
    return(ActivityList) 


def generateActivity() :
    
    chores = ['Wash Dishes', 'Do Laundry', 'Clean Bathroom', 'Walk The Dog', 'Hoover/Sweet Floors']
    fun = ['Watch TV', 'Play a game', 'Have a run', 'Go Swimming', 'Draw/Paint']

    allActivities = chores + fun

    if menu() == 'R' :

        try :
           allList = readFile('all')
           #print(allList) # Testing
           displayOutput(random.choice(allList))

        except FileNotFoundError :
            print('Sorry, all activities list, file not found')
            print('Using default all activities list...\n')
            displayOutput(random.choice(allActivities))

        except :
            print('Sorry there was an error with all.txt')
            print('Using default all activities list...\n')
            displayOutput(random.choice(allActivities))

            #print(allList) # Testing
            #print(type(allList)) # Testing
            #var = traceback.format_exc() # Testing
            #print(var) # Testing

    elif menu() == 'C' :

        try :
            choreList = readFile('chore')
            displayOutput(random.choice(choreList))
            #print(choreList) # Testing

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
            #print(funList) # Testing

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
