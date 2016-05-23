##put at top of whole code/in main function
print('Loading...')
englishWords = open('englishWords.txt','r')
lines = englishWords.readlines()
print('Loaded')


def checkWord(word,englishWords):
    word = word.upper()
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    bottom = 0
    top = 235891
    keepGoing = False
    wordExists = False
    while not wordExists:
        middle = (top + bottom) // 2
        line = lines[middle].upper()
        if alphabet.index(word[0]) > alphabet.index((line[0]).upper()):
            bottom = middle
        elif alphabet.index(word[0]) < alphabet.index((line[0]).upper()):
            top = middle
        else:
            letter = alphabet.index((line[0]).upper())
            top = middle
            bottom = middle
            topFound = False
            bottomFound = False
            break
    while not keepGoing:
        topLine = lines[top].upper()
        bottomLine = lines[bottom].upper()
        if alphabet.index(bottomLine[0]) != letter:
            topFound = True
        if alphabet.index(bottomLine[0]) != letter:
            bottomFound = True
        if not topFound:
            top = top + 1
        if not bottomFound:
            bottom = bottom - 1
        if bottomFound and topFound:
            keepGoing = True
    for i in range(bottom + 1, top):
        if lines[i].upper() == (word + '\n'):
            wordExists = True
    if wordExists:
        print('it exists!')
    else:
        print('bad luck')
    return wordExists
        

checkWord(word,englishWords)
