# import random
# a = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
# b = [random.choice(a)for i in range(15)]
# print(''.join(b))


import random
import sys
strong = int(input('How strong password do you want?\n1-Simple\n2-Strong\n3-Very Strong\n'))
choose = int(input('How many character you want?'))


def choosee(st, ch):
    if st == 1:
        a = 'abcdefghijklmnopqrstuvwxyz'
        if(len(a) >= ch):
            return a
        else:
            sys.exit('Population must be a sequence or set')
    elif(st == 2):
        a = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if(len(a) >= ch):
            return a
        else:
            sys.exit('Population must be a sequence or set')
    elif(st == 3):
        a = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
        if(len(a) >= ch):
            return a
        else:
            sys.exit('Population must be a sequence or set')
    else:
        print('Wrong input..Choose between 1-3')
        sys.exit()


def generate(st, ch):
    n = choosee(st, ch)
    g = random.sample(n, ch)
    v = ''.join(g)
    print(v)


generate(strong, choose)
