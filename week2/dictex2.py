# ramit = {
#     'name': 'Ramit',
#     'email': 'ramit@gmail.com',
#     'interests': ['movies', 'tennis'],
#     'friends': [
#      {
#         'name': 'Jasmine',
#         'email': 'jasmine@yahoo.com',
#         'interests': ['photography', 'tennis']
#
#      },
#      {
#         'name': 'Jan',
#         'email': 'jan@hotmail.com',
#         'interests': ['movies', 'tv']
#      }
#     ]
# }
#
# #PROBLEM 1
# print ramit["email"]
#
# #PROBLEM 2
# print ramit["interests"][0]
#
# #PROBLEM 3
# print ramit["friends"][0]["email"]
#
# #PROBLEM 4
# print ramit["friends"][1]["interests"][1]

#LETTER SUMMARY
# def letterCount(theWord):
#     myDictionary = {}
#     for char in theWord:
#         # print characters
#         if char in myDictionary:
#             myDictionary[char]+=1
#         else:
#             myDictionary[char]=1
#     print myDictionary
#
#
# letterCount("Ilikepizza")

#WORD SUMMARY
def isWhiteSpace(character):
    return character == ' ' or character == '\n'


def slice(sentence):
    words = []
    beginningOfWord = 0
    currentCharacter = 0
    for character in sentence:
        if isWhiteSpace(character):
            words.append(sentence[beginningOfWord:currentCharacter])
            beginningOfWord = currentCharacter + 1
        elif currentCharacter == len(sentence) - 1:
            word = sentence[beginningOfWord:currentCharacter]

        currentCharacter += 1

    return words

def countWords(sentence):
        wordCount = {}
        words = slice(sentence)
        for word in words:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1
        print wordCount


countWords("to be or not to be")
