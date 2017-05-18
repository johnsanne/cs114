""" simple madlib """

print('Tell me a verb.')
VERB = input()
print(VERB)

print('And one more verb, please.')
NIIVERB = input()
print(NIIVERB)

print('I have a question: Who do you hate most?')
HATED = input()
print(HATED)

print('And tell me something you did in the past that you hated doing? (past tense)')
HATEVERB = input()
print(HATEVERB)

print('When you ' + VERB + ', you are going to actually ' + NIIVERB + ' because ' + HATED + ' ' + HATEVERB + '.')
