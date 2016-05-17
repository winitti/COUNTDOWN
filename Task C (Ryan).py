import random
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N','P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y',' Z']
vowels = ['A', 'E', 'I', 'O', 'U',]
letters = []
numberOfConsonants = 0
numberOfVowels = 0
for i in range (0,9):
    while True:
        anyLetter = input('What would you like? You need 6 consonants and 3 vowels. Press 1 for a consonant and 0 for a vowel. ')
        if (anyLetter == '1' and numberOfConsonants < 6):
            letter = consonants[random.randint(0,20)]
            print (letter)
            letters.append(letter)
            print (letters)
            numberOfConsonants = numberOfConsonants + 1
        elif (anyLetter == '1' and numberOfConsonants > 6):
            print ('You cannot add anymore consonants! ')
        if (anyLetter == '0' and numberOfVowels < 3):
            letter = vowels[random.randint(0,4)]
            print (letter)
            letters.append(letter)
            print (letters)
            numberOfVowels = numberOfVowels + 1
        elif (anyLetter == '0' and numberOfVowels > 3):
            print ('You cannot add anymore vowels! ')
    
        
    print (letters)


