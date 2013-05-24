'''
Created on 2013-05-22
@author: Evan
Description: A text based game where you progress by choosing an evolution path
             By the end of the game you must be victorious when you confront
             humans.
Version: 3
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
    
    print ('You are a growing organism in a world full of mysterious  ')
    print ('things, you must make your way up the food chain and survive ')
    print ('your inevitable encounter with humans. The choices ')
    print ('you make will determine your future relationship with ')
    print ('the world, and ultimately whether your species survives. ')

    # wait for user to read the intro story
    time.sleep(7)
    
    # "clear" the screen for effect
    clearScreen()

def clearScreen():
    for clearScreen in range(0,19):
        print (' ')

def choice():
    choice = ''
    while choice != '1' and choice != '2':
        choice = raw_input()
        if choice == '1' or choice == '2':
            print ('...')
        else:
            print ('Please enter the number 1 or 2 as your choice. ')
        
    return choice
    
def evolutionChoices():
    
    win = 'You lost' # tells user if they won
    print ('In order to survive you must evolve. You are fortunate ')
    print ('in your world, because you are able to choose which path ')
    print ('you want to take. ')
    print ('')
    
    time.sleep(6)
    # tier 1 - first decision
    print ('Before you begin evolving, you must decide if you ')
    print ('want more(1) food, or greater varieties(2) of food.')
    choiceMade = choice()
    
    if choiceMade == '1':
        print ('Clearly you want to collect more food to eat. You ')
        print ('should consider going after larger food sources. ')
        time.sleep(3)
    # tier 2 - next decision
        print ('Would you like to improve your strength? Yes(1), No(2) ')
        choiceMade = choice()
        if choiceMade == '1':
            print ('Your strength improves!')
            time.sleep(1)
            print ('You grow in size and become comparable to a bear in strength.')
            time.sleep(1)
            print ('The nearby human village now notices your presence.')
            print ('They start seeing you as a threat to their survival.')
        # tier 3 - next decision
            print ('Would you like a larger jaw and larger teeth? Yes(1), No(2) ')
            choiceMade = choice()
            if choiceMade == '1':
                print ('Humans see you as a large threat to them. You appear as a ')
                print ('monster to them. They fear for their lives so they hunt your species to extinction.')
            else:
                print ('Without greater teeth or a greater jaw, you are just seen ')
                print ('as a large food source to humans. You are now hunted as a food source.')
        else:
            print ('The humans dont find any interest in you. ')
            print ('Would you like larger claws? Yes(1), No(2) ')
            choiceMade = choice()
            if choiceMade == '1':
                print ('Humans see you as a large threat to them. You are not very large, ')
                print ('but they fear for their childrens lives. ')
                print ('As a result they hunt your species to extinction. ')
            else:
                print ('Without greater claws, your species has not developed. ')
                print ('Your species dies out through natural selection. ')
                
            
    else:
        print ('You seem to be the type that likes to excite their ')
        print ('taste buds. You will enjoy having made this decision. ')
        time.sleep(3)
    # tier 2 - next decision
        print ('Would you like to improve your agility? Yes(1), No(2) ')
        choiceMade = choice()
        if choiceMade == '1':
            print ('Your agility improves!')
            time.sleep(1)
            print ('You become more swift and able.')
            time.sleep(1)
            print ('The nearby human village now notices your presence.')
            print ('Your hunting skills increase.')
        # tier 3 - next decision
            print ('Would you like improved stealth? Yes(1), No(2) ')
            choiceMade = choice()
            if choiceMade == '1':
                print ('To become more stealthy you lose weight and shrink.')
                print ('humans see you as a small tiger like animal.')
                print ('They tame you and you live on as a pet.')
                win = 'You won!' # change win value to 'You won'
            else:               # to let the user know
                print ('Due to your lack of stealth, you are hunted by larger animals.')
                print ('You become extinct through natural selection.')
        else:
            print ('The humans dont find any interest in you. ')
            print ('Would you like larger lung capacity for swimming? Yes(1), No(2) ')
            choiceMade = choice()
            if choiceMade == '1':
                print ('You gain additional enemies in the water. As the world changes ')
                print ('your species dies off because it has not evolved down the right path. ')
            else:
                print ('With no evolution, your species has not adapted to the changing world. ')
                print ('Your species dies out through natural selection. ')
            
    return win


def main():
    
    won = 'You lost.'
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        introduction() # call introduction method
        won = evolutionChoices() # pass winning condition to variable won
        
        
    # ask player if they want to play again, accept input
        time.sleep(3)
        print ('')
        print (won) # tell the user if they have won
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()
    # convert answer to lower case to ensure the answer is received correctly
        playAgain = playAgain.lower()


if __name__ == "__main__": main()