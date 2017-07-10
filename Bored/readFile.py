def readFile(list) : 
    """ """ #TODO

       #set permissions for accessing the file
    READ = 'r'
    WRITE = 'w'
    fileName = list + '.txt'

    with open(fileName, READ) as f :
        dictionary = f.readlines() #Reads the entire file

    Activitylist = [word.strip() for word in dictionary] #Seperates each word to create a list of words

            
    return(ActivityList) 
