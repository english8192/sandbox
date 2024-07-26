import random 
from typing import *
from icecream import ic

def cards_pair_or_more(card_list:List) -> Dict[int,int]:
    counts = {card: card_list.count(card) for card in set(card_list)} #turn input card list into a dict with number of instance for each rank
    sorted_counts= {k: counts[k] for k in sorted(counts,reverse=True)} #sort dictionary high card to low card
    remove_singles={k:sorted_counts[k] for k in sorted_counts if sorted_counts[k]>1} #remove any cards that only appear once
        #key = card
        #value = number of instance of card in set(card_list) <— unique values in the original list

    return remove_singles

def quads(card_value_list,dict):
    for key,value in dict.items():
        if value == 4:        
            work_list = [i for i in card_value_list if i!=key]
            quads_list = [i for i in card_value_list if i==key]
            quads_list.append(max(work_list))
            quads_and_kicker= quads_list.copy()
            return (8,quads_and_kicker,"QUADS")
    return

        
def full_house(dict):
    fh_card_values=[]
    work_dict=dict.copy()
    if len(work_dict) > 1:
        for key,value in work_dict.items():
            if value == 3:
                fh_card_values.append(key) #this is bad
                fh_card_values.append(key)
                fh_card_values.append(key)
                work_dict.pop(key)
                break
        if fh_card_values:
            pair_value = list(work_dict.keys())[0]
            fh_card_values.append(pair_value)
            fh_card_values.append(pair_value)
        
            return (7,fh_card_values,"FULL HOUSE")
        else:
            return None

def trips(card_value_list,dict):
    
    for key,value in dict.items():
        if value == 3:        
            work_list = [i for i in card_value_list if i!=key]
            trips_list = [i for i in card_value_list if i==key]
            trips_list.extend(sorted(work_list,reverse=True)[:2])
            trips_and_kickers= trips_list.copy()
            return (4,trips_and_kickers,"TRIPS")
    return

def two_pair(card_value_list,dict):
    tp_card_values=[]
    work_dict=dict.copy()

    if len(work_dict) > 1:
        higher_pair = list(work_dict.keys())[0]
        lower_pair = list(work_dict.keys())[1]
        work_list = [i for i in card_value_list if i!=higher_pair and i != lower_pair]
        tp_card_values.append(higher_pair)
        tp_card_values.append(higher_pair)
        tp_card_values.append(lower_pair)
        tp_card_values.append(lower_pair)
        tp_card_values.append(max(sorted(work_list,reverse=True)))
        return (3,tp_card_values,"TWO PAIR")
    else:
        return None
    
def pair(card_value_list,dict):
# return list(dict.keys())[0] could do this as well
    pair_and_kickers=[]
    if dict:    #will break if the dictionary fed in is empty
        pair=next(iter(dict))
        pair_and_kickers.append(pair)
        pair_and_kickers.append(pair)    
        work_list = [i for i in card_value_list if i!=pair]
        pair_and_kickers.extend(sorted(work_list,reverse=True)[:3])    
        return (2,pair_and_kickers,"PAIR") # this skips creating an intermediary list and just uses a iter object
    else:
        return None


def find_multi_hand(card_value_list: List[int]) -> Tuple[str,Union[List,int]]:
    #get the frequency dictionary from the input list
    freq_dict = cards_pair_or_more(card_value_list)
    #ic(freq_dict)


    quads_result      = quads(card_value_list,freq_dict)
    full_house_result = full_house(freq_dict)
    trips_result      = trips(card_value_list,freq_dict)
    two_pair_result   = two_pair(card_value_list,freq_dict)
    pair_result       = pair(card_value_list,freq_dict)
    #ic(freq_dict)

    if not freq_dict: #if no pairs or more are found ie freq_dict is empty, return the highest card
        high_card_result = (1,sorted(card_value_list,reverse=True)[:5],"HIGH CARD",)
        return high_card_result
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
    

