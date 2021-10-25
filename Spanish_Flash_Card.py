import os, random, sys, EnSp, SpEn, EntoSp, SptoEn

print('this is a Spanish Flash Card Program')
print('A Spanish word will Appear on the screen, see if you can guess the English equivelant')
input('press Enter To Start:')

def properFlashCards():
    v = 1
    print('Press the Escape Sequence to exit. (Ctrl+c)\n\n')
    input('Guess the English translation of this word: \n')
    while v:
        i = random.randint(0,308)
        s = SpEn.SpEn[i]
        c = SptoEn.SptoEn[s]
        input(SpEn.SpEn[i]+'\n')
        print(c+'\n\n')
properFlashCards()

# how to cycle the program so that each keystroke = function runs


'''
Okay billionare, what would you like me to do? Is there going to be anymore painful give and takes from trying to interpret cryptic telepathic messages rather 
    than just being normal and saying hi, and introducing yourself to someone, I have an insurmountable level of shame. I have been homeless (personally 
    my most hated characteristic is the inability to provide for myself, or show that I've attained anything, or achieved anything, or have any friends
    or have anything good offer anyone. I understand I'm a liability, I understand that I've been homeless so long that it merits someone introducing them-
    selves to me rather than I to them in terms of ability and agreeability and social grace. I'm deficient in every conceivable way. Ashamed of how I look
    ashamed at my life long lack of friends, support, residence, the ability to provide, social acceptance and society only ever makes more demands on me.
    So, if you want me to follow yet another series of cryptic telepathic demands from you, perhaps you should just accept the fact that I will only ever
    focus on what is right and appropriate and in this period of time, understanding that the skills that I'm deficient in, the friends that I've never hated
    that have never housed me, that have never cared to ask whether or not I was properly fed or adequetaly clothed I must somehow attain, because I am getting
    older I need to focus on my health and because my life has only ever been a repetitive course of how much a particular oponent can take from me I need to 
    focus on achieving my goals. It's a matter of life and death for me. A person's education is built over years of dedication. An athlete is trained over 
    completing smaller tasks systematically to acquire an advanced skill set...and the more people I meet, the more I find that I know nothing at all. That 
    if I had the support or the strength or the proper upbringing or the right mentors or the right skills, then what I'm experiencing now would have been 
    impossible. With everything I have left, and as of this day it is one backpack, I have to push forward for success...and this night, despite it being my 
    35th birthday, that means I must accomplish my goals.
'''