from typing import *
from collections import defaultdict



def get_suits(card_list):
    suit_tup_list=[(k.value, k.suit) for k in card_list]
    suit_tup_list=sorted(suit_tup_list,reverse=True)
    return suit_tup_list

def split_suits(suit_tup_list):
    grouped_data = defaultdict(list)
    for i in suit_tup_list:
        suit=i[1]
        grouped_data[suit].append(i)
    grouped_data = dict(grouped_data)
    return grouped_data

def count_suits(grouped_data):
    count_dict={k:len(v) for k,v in grouped_data.items()}
    return count_dict
    




def flush(card_list):
    ungrouped_suits=get_suits(card_list)
    print(ungrouped_suits)
    grouped_suits = split_suits(ungrouped_suits)
    print(grouped_suits)
    counted_suits=count_suits(grouped_suits)
    return counted_suits