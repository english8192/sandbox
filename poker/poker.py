import random
from icecream import ic

import multi_hand,straight,flush,straight_flush



class Card:
    ranks = {"A":14,'K':13,'Q':12,'J':11, 'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
    suits = {'H':'Hearts','S':'Spades','C':'Clubs','D':'Diamonds'}
    def __init__(self, rank, value, suit, suitname):
        self.rank = rank
        self.value = value
        self.suit = suit
        self.suitname = suitname

# class Hand:

    
class Deck(list):
    def __init__(self):
        self.populate_deck()
        
    def populate_deck(self):
        self.clear()
        for rank in Card.ranks:
            value=Card.ranks[rank]
            for suit in Card.suits:
                suitname=Card.suits[suit]
                card=Card(rank,value,suit,suitname)
                self.append(card)

                
    def get_card_info(self,card):
        #card_info=f"rank:{card.rank}\nvalue:{card.value}\nsuit:{card.suitname}\n"
        card_info = f"{card.rank} of {card.suitname}\n"
        return card_info
    
    def shuffle(self,n=52):
        self.populate_deck()
        shuffle_list=[]
        while len(shuffle_list) < 52:
            n-=1

            random_index=random.randint(0,n)
            shuffle_list.append(self[random_index])
            self.remove(self[random_index])
            #print(f"unshuff list: {len(self)}  shuffled list: {len(shuffle_list)}")

        self[:]=shuffle_list
        return self
    

    def draw(self,num_cards,location):
        for i in range(0,num_cards):
            location.append(self[i])

            self.remove(self[i])
        return location

        

class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]
        self.stack=0
        self.status=''
        self.hand_info=None
        self.role = None
        self.infront = 0
    def discard(self):
        self.hand=[]
        self.hand_info=None
        #self.role = None
        self.status = None

    def bet(self,amount):
        self.infront= amount
        self.stack -= amount
    
        

    
class Community:
    def __init__(self):
        self.flop=[]
        self.turn= []
        self.river= []
        self.seven_cards=[]
        
    def draw_flop(self,deck):
        self.flop=deck.draw(3,self.flop)

    def draw_turn(self,deck):
        deck.draw(1,self.turn)
    def draw_river(self,deck):
        deck.draw(1,self.river)

    def get_seven_cards(self,player):
        self.seven_cards=[] # reinitialize each time the method is called to prevent accumulation from previous method calls
        self.seven_cards.extend(player.hand)
        self.seven_cards.extend(self.flop)
        self.seven_cards.extend(self.turn)
        self.seven_cards.extend(self.river)
        #self.seven_cards = [item for sublist in self.seven_cards for item in sublist] #self.seven_cards will be a list of lists due to the flop turn and river being list so we have to flatten it

        return self.seven_cards
    def discard(self):
        self.flop=[]
        self.turn= []
        self.river= []
        self.seven_cards=[]
        




def get_values(card_list):
    v_list=[]
    for card in card_list:
        v_list.append(card.value)
    return v_list


def determine_hand(player,players_seven):
    hand_result=None
    player_and_comm_cards=players_seven
    value_list=get_values(player_and_comm_cards)
    #ic(value_list)
    flush_result = flush.find_flush(player_and_comm_cards)
    straight_result = straight.find_straight(value_list)
    straight_flush_result = straight_flush.find_straight_flush(flush_result, straight_result)

    if straight_flush_result:
        hand_result = straight_flush_result
    elif flush_result:
        hand_result = flush_result
    elif straight_result:
        hand_result = straight_result
    else:
        multi_hand_result = multi_hand.find_multi_hand(value_list)
        hand_result = multi_hand_result


    player.hand_info = hand_result
    return hand_result


def determine_winner(player_list):
    current_hands = {player.name:player.hand_info for player in player_list}
    sorted_list= sorted(current_hands.items(),key = lambda x:x[1],reverse=True) #sort by second item (skips the name value in the dict.items)
    top_fivecard_hand = sorted_list[0][1][1]    #finds the best five card hands of the players (may be held by more than one player)
    top_hands = [i for i in sorted_list if i[1][1] == top_fivecard_hand] #gets all players who hold that best hand (to find ties)

    if len(top_hands) > 1:
        winner = top_hands
        return winner

    winner = sorted_list[0]
    return winner



def display_player_card_info(player,seven_cards):
    print(f"----------------{player.name}---------------")
    for card in seven_cards: 
        print(deck.get_card_info(card))


# if __name__ == "__main__":