'''
Created on 2013-05-22
@author: Evan
Description: text based game where you progress by choosing an evolution path
             By the end of the game you must be victorious when you confront
             humans.
'''
import time

def introduction():
    # brief instructions on how to play the game before it starts
    print ('Instructions:')
    print ('Enter the number 1 or 2 corresponding to your evolution choice.')
    
    # wait for user to read instructions
    time.sleep(7)

    # "clear" the screen for effect
    clearScreen()

def clearScreen():
    for clearScreen in range(0,19):
        print (' ')
        
    
def evolutionChoices():
    # first evolutionary path
    choice = ''
    victory = 0 # if the user chooses correctly, this value will increase
                # to win, the user must attain a certain victory point value
    while choice != '1' and choice != '2':
        print ('Would you like to improve your strength(1) or intelligence(2)?')
        
        choice = raw_input()
        
        if choice == '1':
            victory = victory - 1
            print ('You have chosen strength!')
            time.sleep(1)
            print ('You grow in size and become comparable to a bear in strength.')
            time.sleep(1)
            print ('The nearby human village now notices your presence.')
            print ('They start seeing you as a threat to their survival.')
        else:
            victory = victory + 1
            print ('')
            
    return choice, victory

def checkchoice(chosen):
    
    if chosen == '1':
        print ('test')
    else:
        print ('testFail')
    
    print ('')
    time.sleep(1)
    print ('')
    time.sleep(1)
    print ('')
    print
    time.sleep(1)
    
    '''friendlyChoice = 
    
    if chosen == str(friendlyCave):
        print ('Gives you his treasure!')
    else:
        print ('Gobbles you down in one bite!')
'''


def main():
    
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        introduction() # call introduction method
        evolutionNumber = evolutionChoices() # assign the choice return value from firstChoice method to evolutionNumber
        checkchoice(evolutionNumber[0]) # send evolutionNumber choice value to be checked
        
    # assign the second returned variable - victory points
        totalVictoryPoints = evolutionNumber[1]
        
        print (totalVictoryPoints)
    # ask player if they want to play again, accept input
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()
    # convert answer to lower case to ensure the answer is received correctly
        playAgain = playAgain.lower()


if __name__ == "__main__": main()