import random
import multi_hand,straight,flush


class Card:
    ranks = {"A":14,'K':13,'Q':12,'J':11, 'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
    suits = {'H':'Hearts','S':'Spades','C':'Clubs','D':'Diamonds'}
    def __init__(self, rank, value, suit, suitname):
        self.rank = rank
        self.value = value
        self.suit = suit
        self.suitname = suitname
    
class Deck(list):
    def __init__(self):
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
        shuffle_list=[]
        while len(shuffle_list) < 52:
            n-=1

            random_index=random.randint(0,n)
            shuffle_list.append(self[random_index])
            self.remove(self[random_index])
            #print(f"unshuff list: {len(self)}  shuffled list: {len(shuffle_list)}")

        self[:]=shuffle_list
        return shuffle_list
    

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

        
def get_values(card_list):
    v_list=[]
    for card in card_list:
        v_list.append(card.value)
    return v_list


        
deck=Deck()

deck.shuffle()


bob=Player("BOB")
dick=Player("DICK")
john=Player("JOHN")

player_list=[bob,dick,john]

community=Community()

for player in player_list:
    deck.draw(2,player.hand)




community.draw_flop(deck)
community.draw_turn(deck)
community.draw_river(deck)



#bob_all=community.get_seven_cards(bob)
# dick_all=community.get_seven_cards(dick)
# john_all=community.get_seven_cards(john)


def player_card_info(player):
    print(f"----------------{player.name}---------------")
    all=community.get_seven_cards(player)
    for card in all: 
        print(deck.get_card_info(card))

    value_list=get_values(all)
    print(value_list)

    print(flush.flush(all))


    straight_status=straight.find_straight(value_list)
    multi_hand_status=multi_hand.find_multi_hand(value_list)
    print("\n")
    if straight_status:
        print(straight_status)
    else:
        print(multi_hand_status)

for player in player_list:
    player_card_info(player)







# print(f"Deck size: {len(deck)}\n")
# print(f"bob's hand size:{len(bob.hand)}\n")

# for card in bob.hand:
#     print(deck.get_card(card))








































# class Deck(self):
#     shuffle
#     draw



# class Player(self):


# class Hand(self):

# class Community(self):
