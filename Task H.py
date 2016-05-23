#because not all the code is combined, i am using a random number for a score and using random code as the game (for repeating again)

score = 59
highestscore = 78
gamecounter = 0

#remove this def game in the main code, i am just using random code for the game
def game():
    examplename = input('What is your name? ')
    print ('Hello ', examplename, ", let's play!")

def runningthegame():
    gamecounter = 0
    for i in range (0,3):
        gamecounter = gamecounter + 1
        game()
        print ('You have played the game ', gamecounter, 'times')
        print ('Your score was.. ', score,'. The highest score was... ', highestscore)

def main():
    runningthegame()

main()

wouldyouliketoplayagain = input('Would you like to play the game again? ')
if wouldyouliketoplayagain == 'yes':
    main()
if wouldyouliketoplayagain == 'no':
    print ('aight')
  


