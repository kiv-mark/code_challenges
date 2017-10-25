"""
Here the input will be height the prisoner jumps, height the prisoner slips after every jump, the number of walls, and the height of each wall.
We have to find the number of attempt the prisoner takes to cross all the walls.

"""
import os, sys

def GetJumpCount(jumps, slips, heights=[]):

    global attempt
    attempt = 0
    no_of_walls = len(heights)
    for i in heights:
        if jumps == i:
            attempt = attempt + 1
        
        else:
            attempt = attempt+1
            dum_jumps = jumps
            while dum_jumps < i:
                new_jumps = dum_jumps - slips
                dum_jumps = new_jumps + dum_jumps - slips
                attempt = attempt+1
            
    return attempt

ip1 = int(raw_input());
ip2 = int(raw_input());
ip3_cnt = 0
ip3_cnt = int(raw_input())
ip3_i=0
ip3 = []
while ip3_i < ip3_cnt:
    ip3_item = int(raw_input());
    ip3.append(ip3_item)
    ip3_i+=1
output = GetJumpCount(ip1,ip2,ip3)
print(str(output))
