#Here we gonna do the functions we need to do that

def toLowerCase(text):
    '''First we need to set every word to lower case, to avoid problems with capital letters'''
    setText = text.lower()
    return setText

def cleanText(setText):
    '''Now we need to remove all the punctuation marks, so we can count the words'''
    cleanText = setText.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    return cleanText

def splitText(cleanText):
    '''Now we need to split the text into words, so we can count them'''
    splitText = cleanText.split(" ")
    return splitText

def countedWords(splitText):
    '''Now with this funtion we will count the words'''
    count = {} #We create a dictionary to store the words and their count
    for word in splitText:
        if word in count:
            count[word] += 1 #If the word is already in the dictionary we add 1 to the count
        else:
            count[word] = 1 #If the word is not in the dictionary we add it and set the count to 1
    return count





    
