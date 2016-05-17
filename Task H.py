#because not all the code is combined, i am using a random number for a score and using random code as the game (for repeating again)

score = 59
highestscore = 78
gamecounter = 0


gamecounter = gamecounter + 1
examplename = input('What is your name? ')
print ('Hello ', examplename, ", let's play!")
print ('You have played the game ', gamecounter, 'times')
print ('Your score was.. ', score,'. The highest score was... ', highestscore)
wouldyouliketoplayagain = input('You need to play the game 3 times, and you have played it ', gamecounter, 'times. Would you like to follow the rules? (You can always be a rebel and quit now) ')
if (wouldyouliketoplayagain == 'yes'and gamecounter < 3):
    print ('aight')
if (wouldyouliketoplayagain == 'yes' and gamecounter >=3):
    print ('You already have played this game more than three times!')


    
    

