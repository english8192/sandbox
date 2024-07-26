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



def assign_roles(player_list): #convert parts of this using map()
    x=(len(player_list)-3)
    if not [i.role for i in player_list if i.role != None]: #if no roles have been set yet
        ic("first time set")
        player_list[0].role="DEALER"
        player_list[1].role="LITTLE"
        player_list[2].role="BIG"


        for player in player_list:
            if player.role == None:
                player.role = f"D-{x}"
                x-=1
    else:
        ic("every subsequent set")
        temp_role=[]
        for player in player_list:
            new_role_index = (((player_list.index(player))-1) % len(player_list))

            temp_role.append(player_list[new_role_index].role)
            

        for player in player_list:
            player.role = temp_role[player_list.index(player)]

    print("after move")
    for player in player_list:
        ic(player.name,player.role)
    print("\n")


# def assign_roles2(player_list): #convert parts of this using map()
#     x=(len(player_list)-3)
#     if not [i.role for i in player_list if i.role != None]: #if no roles have been set yet
#         ic("first time set")
#         player_list[0].role="DEALER"
#         player_list[1].role="LITTLE"
#         player_list[2].role="BIG"


#         for player in player_list:
#             if player.role == None:
#                 player.role = f"D-{x}"
#                 x-=1
#     else:
#         print("subsequent moves")
#         rolelist1= [player.role for player in player_list]
#         ic(rolelist1)
#         rolelist2 = [rolelist1[rolelist1.index(((x-1)%(len(rolelist1))))] for x in range((len(rolelist1)))]

#         ic(rolelist2)

#     print("after move")
#     for player in player_list:
#         ic(player.name,player.role)
#     print("\n")






def move_role_chips(player_list):
    player_list



deck.shuffle()
assign_roles(player_list)
assign_roles(player_list)

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





