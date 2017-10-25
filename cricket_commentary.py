"""
we have to simulate a cricket match. 4 overs remaining, and 40 runs to win. only 4 wickets left.
"""

import random

print "Sample commentary"
print "4 overs left. 40 runs to win"

players = {
              "Virat Kohli" : [],
              "MS Dhoni" : [],
              "Bumrah" : [],
              "Ashish Nehra" : []
          }

player_list = ["Virat Kohli", "MS Dhoni", "Bumrah", "Ashish Nehra"]
dict_wicket = {"Virat Kohli" : 1, "MS Dhoni" : 1, "Bumrah" : 1, "Ashish Nehra" : 1}

total = 0
flag_result = False
out_list = []


def score(batsman):

    val = random.randint(0,7)

    if val == 7:
        print batsman+" is out."
        player_list.remove(batsman)
        swap_batsman()
        return val
    else:
        print batsman+" scored in this ball = "+str(val)
        return val
    
def batsman():

    for i in player_list:

        if 7 in players[i]:
            pass
        else:
            return (i)

def swap_batsman():

    for i in player_list:
        if 7 in players[i]:
            pass
        else:
            try:
                index_val = player_list.index(i)
                dummy = player_list[index_val]
                player_list[index_val] = player_list[index_val+1]
                player_list[index_val+1] = dummy
                return True
            except:
                return False

#import pdb; pdb.set_trace()

for over in range(4):

    for ball in range(6):

        if len(player_list) > 1:
            pass
        else:
            break

        batsman_name = batsman()
        score_data = score(batsman_name)

        if score_data == 7:
            score_data = 0
       
        if score_data == 1 or score_data == 3 or score_data == 5:
            swap_var = swap_batsman()
        else:
            swap_var = True

        if swap_var == False:
            break

        total = total+score_data
        if total > 40 or total ==40:
            break

    else:
        print "Over done"
        remaining_runs = 40 - total
        remaining_over = 4 - (over+1)
        print str(remaining_over)+" overs left. "+str(remaining_runs)+" runs to win"
        swap_batsman()
        print "Enter to continue the over...!!!"
        raw_input()
        
    if swap_var == False:
        flag_result == False

    if total > 40 or total ==40:
        flag_result = True
        break

    if len(player_list) > 1:
        pass
    else:
        flag_result == False
        


if flag_result is True:
    print "India wins by "+str(len(player_list))+" wickets"
else:
    print "India loss by "+str(40 - total)+" runs"
