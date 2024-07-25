from flush import find_flush
from straight import find_straight
from icecream import ic

def find_straight_flush(flush_result,straight_result):

    if flush_result and straight_result:
        ic(flush_result)
        ic(straight_result)
        ic("Both  XXX straight and flush")
        return 1
