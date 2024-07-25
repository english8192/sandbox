from flush import find_flush
from straight import find_straight
from icecream import ic

def find_straight_flush(flush_result,straight_result):
 
    
    if flush_result and straight_result: #check that both both a straight and flush were hit (not necessarily the same set of 5 for both)

        flush_value_list = flush_result[1] # get the list of values from the straight and flush 5 cards
        straight_value_list = straight_result[1]

        if flush_value_list == straight_value_list: #compare them
            straight_flush_result = ("Straight Flush",flush_result[0][0],straight_result[0][1])
            return straight_flush_result
