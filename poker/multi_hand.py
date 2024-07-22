import random 
from typing import *

def cards_pair_or_more(card_list:List) -> Dict[int,int]:
    counts = {card: card_list.count(card) for card in set(card_list)} #turn input card list into a dict with number of instance for each rank
    sorted_counts= {k: counts[k] for k in sorted(counts,reverse=True)} #sort dictionary high card to low card
    remove_singles={k:sorted_counts[k] for k in sorted_counts if sorted_counts[k]>1} #remove any cards that only appear once
        #key = card
        #value = number of instance of card in set(card_list) <— unique values in the original list

    return remove_singles

def quads(dict):
    for key,value in dict.items():
        if value == 4:
            return ("quads",key)
        
def full_house(dict):
    fh_card_values=[]
    work_dict=dict.copy()
    if len(work_dict) > 1:
        for key,value in work_dict.items():
            if value == 3:
                three_fh=key
                fh_card_values.append(three_fh)
                work_dict.pop(key)
                break
        if fh_card_values:
            fh_card_values.append(list(work_dict.keys())[0])
            return ("full house",fh_card_values)
        else:
            return None

def trips(dict):
    for key,value in dict.items():
        if value == 3:
            return ("trips",key)
        
def two_pair(dict):
    tp_card_values=[]
    work_dict=dict.copy()
    if len(work_dict) > 1:
        tp_card_values.append(list(work_dict.keys())[0])
        tp_card_values.append(list(work_dict.keys())[1])
        return ("two pair", tp_card_values)
    else:
        return None
def pair(dict):
# return list(dict.keys())[0] could do this as well

    if dict:    #will break if the dictionary fed in is empty
        pair=next(iter(dict))
        return ("pair", pair) # this skips creating an intermediary list and just uses a iter object
    else:
        return None


def find_multi_hand(card_value_list: List[int]) -> Tuple[str,Union[List,int]]:
    #get the frequency dictionary from the input list
    freq_dict = cards_pair_or_more(card_value_list)


    quads_result      = quads(freq_dict)
    full_house_result = full_house(freq_dict)
    trips_result      = trips(freq_dict)
    two_pair_result   = two_pair(freq_dict)
    pair_result       = pair(freq_dict)
    print(freq_dict)
    if not freq_dict: #if no pairs or more are found ie freq_dict is empty, return the highest card
        return ("high card",max(card_value_list))

    elif quads_result:
        return quads_result
    
    elif full_house_result:
        return full_house_result
    
    elif trips_result:
        return trips_result
    
    elif two_pair_result:
        return two_pair_result

    elif pair_result:
        return pair_result
    

