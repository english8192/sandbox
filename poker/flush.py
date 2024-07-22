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
    count_dict={k:len(v) for k,v in grouped_data.items() if len(v) >= 5}
    if count_dict:
        print("FLUSH FLUSH FLUSH FLUSH\nFLUSH FLUSH FLUSH FLUSH")
        flush_suit=list(count_dict.keys())[0]
        print(flush_suit)
        flush_high_rank=grouped_data[flush_suit][0][0] #access firs item of list for specific suit, access the rank of the first item, it should already be sorted highest to lowest rank.
        return flush_suit, flush_high_rank
    return None
# fix arw
#   File "c:\Users\english\Desktop\repos\poker\flush.py", line 23, in count_suits
#     flush_high_rank=list(count_dict[flush_suit])[0][0] #access firs item of list for specific suit, access the rank of the first item, it should already be sorted highest to lowest rank.
#                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: 'int' object is not iterable


def flush(card_list):
    ungrouped_suits=get_suits(card_list)
    print(ungrouped_suits)
    grouped_suits = split_suits(ungrouped_suits)
    print(grouped_suits)
    counted_suits=count_suits(grouped_suits)
    return counted_suits

