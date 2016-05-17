def menu():
    Name = input("Please enter your name")
    print("Hello",Name,"welcome to my game")
    endOfGame = False
    while endOfGame == False:
        print("Press 1 to play")
        print("Press 2 to quit")
        anyInput = input("Please choose an option ")
        if anyInput == '1':
            game()
        else:
            print("Bye!")
            endOfGame = True
        
            
    

menu()
    
    
    
