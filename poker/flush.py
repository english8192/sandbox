from typing import *
from collections import defaultdict
from icecream import ic



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
    count_dict={k:len(v) for k,v in grouped_data.items() if len(v) >= 5}
    if count_dict:
        #ic("FLUSH FLUSH FLUSH FLUSH")
        flush_suit=list(count_dict.keys())[0]
        #ic(flush_suit)
        flush_high_rank=grouped_data[flush_suit][0][0] #access first item of list for specific suit, access the rank of the first item, it should already be sorted highest to lowest rank.
        return flush_suit, flush_high_rank
    return None

def find_flush(card_list):
    ungrouped_suits=get_suits(card_list)
    #ic(ungrouped_suits)
    grouped_suits = split_suits(ungrouped_suits)
    #ic(grouped_suits)
    counted_suits=count_suits(grouped_suits)
    return counted_suits

