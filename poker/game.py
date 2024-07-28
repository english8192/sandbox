import random 
from icecream import ic
import poker as p


deck=p.Deck()

bob=p.Player("BOB")
dick=p.Player("DICK")
john=p.Player("JOHN")
stanley=p.Player("STANLEY")
michael=p.Player("MICHAEL")
tom=p.Player("TOM")
gomer=p.Player("GOMER")
fritz=p.Player("FRITZ")


player_list=[bob,dick,john,stanley,michael,tom,gomer,fritz]



def get_player_by_role(role,dict):        
    player=dict[role]
    ic(player.name)
    return player




def assign_roles(player_list): #convert parts of this using map()
    x=(len(player_list)-3)
    if not [i.role for i in player_list if i.role != None]: #if no roles have been set yet
        player_list[0].role="DEALER"
        player_list[1].role="LITTLE"
        player_list[2].role="BIG"
        for player in player_list:
            if player.role == None:
                player.role = f"D-{x}"
                x-=1
        role_dict = {player.role:player for player in player_list} 
        return role_dict

    else:
        rolelist_current= [player.role for player in player_list] #list of players current roles
        rolelist_next = [rolelist_current[(((rolelist_current.index(x))-1)%len(rolelist_current))] for x in rolelist_current] #create a new list that shifts the role back one index position
        for player, role in zip(player_list,rolelist_next): #assign the players the newly shifted roles
            player.role = role 
        role_dict = {player.role:player for player in player_list} 
        return role_dict

    # #just for display  
    # print("after move")
    # for player in player_list:
    #     ic(player.name,player.role)
    # print("\n")





def give_stacks(player_list,amount):
    for player in player_list:
        player.stack = amount
        

role_dict=assign_roles(player_list)
give_stacks(player_list, 10000)



get_player_by_role("LITTLE").infront = 50
deck.shuffle()

community=p.Community()
community.draw_flop(deck)
community.draw_turn(deck)
community.draw_river(deck)
hand_type_list=[]
for player in player_list:
    deck.draw(2,player.hand)

    players_seven = community.get_seven_cards(player) # Could potentially move this into the determine() function

    #display_player_card_info(player,players_seven) #just for display
    hand_type=p.determine_hand(player,players_seven)
    hand_type_list.append(hand_type)
    # ic(player.name,player.hand_info)

winner=p.determine_winner(player_list)
ic(winner)
    
for player in player_list: 
    player.discard()

community.discard()
print("\n")


#------------------------------------------------------------------------------------------------------------------
'''
bigblind=100
littleblind=50

1. player












'''


