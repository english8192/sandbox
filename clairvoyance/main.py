import random
import numpy
from icecream import ic
opal_stack = 1000
ivan_stack = 1000

ivan_hand = None
opal_hand = None

card_list = [1,2,3]
count=0



def get_winner(opal_hand,ivan_hand):
    if opal_hand > ivan_hand:
        return "opal"
    else:
        return "ivan"
    
def deal():
    card_list = [1,2,3]
    opal_hand = card_list[random.randint(0,2)]
    card_list.remove(opal_hand)
    
    ivan_hand = card_list[random.randint(0,1)]
    card_list.remove(ivan_hand)

    return opal_hand,ivan_hand

def ivan_first_decision(ivan_hand):
    if ivan_hand == 3:
        return "raise"
    elif ivan_hand == 2:

        if random.random() < 0.5:
            return "raise"
        else: 
            return "check"

    elif ivan_hand == 1:
        if random.random() < 1:
            return "raise"
        else: 
            return "check"


def opal_decision(opal_hand,ifd):
    if opal_hand == 3 and ifd == "raise":
        return "call" 
    elif opal_hand == 3 and ifd == "check":
        return "check"
    elif opal_hand == 2 and ifd == "raise":
        if random.random() < 0.25:
            return "call"
        else: 
            return "fold"
    elif opal_hand == 2 and ifd == "check":
        return "check"
    elif opal_hand == 1 and ifd == "raise":
        return "fold"
    elif opal_hand == 1 and ifd == "check":
        return "check"

olist=[]
ilist=[]
while opal_stack > 0 and ivan_stack >0:
    otemp_stack= opal_stack
    itemp_stack = ivan_stack
    dealt_cards = deal()
    opal_hand = dealt_cards[0]
    ivan_hand = dealt_cards[1]
    if opal_hand == ivan_hand:
        print("FUCK")
        break
    ifd = ivan_first_decision(ivan_hand)
    od= opal_decision(opal_hand,ifd)


    # ic(opal_hand)
    # ic(ivan_hand)
    # ic(ifd)
    # ic(od)



    ivan_stack -= 1
    opal_stack -= 1 #ante
    pot=2

    if ifd == "raise" and od == "call":
        ivan_stack -= 1
        opal_stack -= 1

        pot += 2
        winner_stack=get_winner(opal_hand,ivan_hand) 
        if winner_stack == "opal":
            opal_stack += pot
        elif winner_stack == "ivan":
            ivan_stack += pot 

        # ic()

    elif ifd == "raise" and od == "fold":
        ivan_stack += pot
        # ic()

        
    elif ifd == "check":
        winner_stack=get_winner(opal_hand,ivan_hand) 
        if winner_stack == "opal":
            opal_stack += pot
        elif winner_stack == "ivan":
            ivan_stack += pot 


    count  +=1
    olist.append(opal_stack - otemp_stack)
    ilist.append(ivan_stack - itemp_stack)
ic(count)
ic(opal_stack)
ic(ivan_stack)
opal_roc=f"{numpy.mean(olist):.2f}"
ivan_roc=f"{numpy.mean(ilist):.2f}"
ic(opal_roc)
ic(ivan_roc)
    










