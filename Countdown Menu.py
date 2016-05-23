import time
def menu():
    Name = input("Please enter your name ")
    print("Hello",Name,"welcome to COUNTDOWN!")
    time.sleep(2)
    endOfGame = False
    while endOfGame == False:
        print("Press 1 to play")
        time.sleep(2)
        print("Press 2 to quit")
        time.sleep(2)
        anyInput = input("Please choose an option ")
        if anyInput == '1':
            game()
        else:
            print("Bye!")
            endOfGame = True
        
            
    

menu()
    
    
    
