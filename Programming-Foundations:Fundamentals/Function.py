# This is a problem I took it from code war And I solved it and make some changes on it
# you have some aimo each dragon need to aimo to die so you will take number of aimo and number of dragons 
# And you shiuld tell us if the hero ell win or lose
def Hero(aimo,dragons):
    if aimo > dragons *2 :
        return "Hero will win"
    else:
        return "Hero will lose"



print(Hero(50, 25))


