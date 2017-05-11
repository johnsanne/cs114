
print('Hey there. What are you, a vampire?????')

inquire_vampire = input()

if inquire_vampire == 'yes':
    print('Ahhhh! I knew it! So you are a vampire.')
    print('So then, you must be pretty freaking old. How many years have you been alive, huh??')
    age = int(input())
    if (age < 100):
        print('Hmmmm..... are you really a vampire???')
    elif (age > 100):
        print('HA HA HA. So you are!')

elif inquire_vampire == 'no':
    print('Ah, darn, I was hoping I had finally met a real life vampire.')
