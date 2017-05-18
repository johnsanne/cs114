def sleep():
    import time
    time.sleep(2)


print('Ask the magic 8 ball a yes or no question.')

question = input()

sleep()
print('So your question is... ' + question)

sleep()

print('.....')
sleep()

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Just give up'
    elif answerNumber == 2:
        return 'Probably not what you want'
    elif answerNumber == 3:
        return 'No'
    elif answerNumber == 4:
        return 'Really not feeling it'
    elif answerNumber == 5:
        return 'Bees?'
    elif answerNumber == 6:
        return 'Are you sure you really need an answer?'
    elif answerNumber == 7:
        return 'lolololol'
    elif answerNumber == 8:
        return 'Die'
    elif answerNumber == 9:
        return 'Looking a little dark'

#r = random.randint(1, 9)
#fortune = getAnswer(r)
#print(fortune)

print(getAnswer(random.randint(1,9)))
