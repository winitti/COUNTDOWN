letters =[]
word = ''
def check():
    for i in range(0,len(word)):
        if word[i] not in letters:
            return False
            break
        return True

check()
        
