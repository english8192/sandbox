import random
from typing import *
from icecream import ic


def find_straight(card_value_list: List[int]) -> List[int]:
    seven_cards = card_value_list
    seven_cards = list(set(seven_cards))    # remove duplicate cards
    seven_cards.sort(reverse=True) # sort high to low
    seven_cards1=enumerate(seven_cards)
    seven_cards2=enumerate(seven_cards)
    seven_cards_list=list(seven_cards2)   # create list of tuple from enum object to use for indexing later

    spaces_sum=0 # reset count
    ace_straight=[14,2,3,4,5]

    straight_list=[]


    for index,card_value in seven_cards1:
        if index < len(seven_cards) - 1:
        
            space = card_value - seven_cards_list[index+1][1]
            if space == 1 :

                spaces_sum += space
                straight_list.append(card_value)
                if spaces_sum == 4:
                    straight_list.append(seven_cards_list[index+1][1])
                    break
            else:
                spaces_sum = 0
                straight_list=[]

    if len(straight_list) == 5:
        #ic("Other straight")
        straight_result = ("STRAIGHT", straight_list)
        return straight_result

        
    elif all(card in seven_cards for card in ace_straight): #hard check for A2345
        #ic("Ace straight")
        straight_result = ("STRAIGHT", straight_list)
        return straight_result
    else:
        return




# start at the largest value should always return the higher straight if you have more than one
#reset the spaces_sum if there is any space bigger than one rank, this ensures that hands like 2,3,4,7,9,K,A don't count just because they have 4 gaps of 1 rank not in a row.
# convert to set first to remove dupe cards that will throw off the space finder --> these will reset the spaces_sum
    #I could maybe do if space == 0 just ignore it and keep going?



# def get_sample(size):
#     l=[2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14]
#     sample=[]
#     for i in range(size):
#         card=random.choice(l)
#         l.remove(card)
#         sample.append(card)
#     return sample
