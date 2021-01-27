import random

dice=input("Which Type of dice do you need?\nOptions are:\ntwo sided die\nfour sided die\nsix sided die\neight sided die\nten sided die\ntwenty sided die\nPlease choose here:\nnote: please write out the word rather than type the number i.e if you want a 6 sided die you need to write '6 sided die'")
valmin=1

if dice=='two sided die':
    valmax=2
elif dice=="four sided die":
    valmax=4
elif dice=="six sided die":
    valmax=4
elif dice=="eight sided die":
    valmax=8
elif dice=="ten sided die":
    valmax=10
    #please note that this is not a complete DND set, hopefully it will be soon
elif dice=="twelve sided die":
    valmax=12
elif dice=="twenty sided die":
    valmax=20

again=True

while again:
    print(random.randint(valmin,valmax))
    another_roll=input("Would you like to roll again? ")
    if another_roll.lower()=='yes'or another_roll.lower()=='y':
        continue
    else:
        break


#https://datascienceunlimited.tech/step-by-step-coding-a-dice-roll-simulator-in-python/ 
#^website that mainly wrote lines 22-30
#goodbyeworld