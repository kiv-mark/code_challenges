"""
Any army official sends his coordinates in a encrypted message. He will send the size of the code, and the size of long message. After that he will send the code and the message. We have to find the number of times code that appears in the message. The code can be an anagram. Example: cAdb, and dcAb means same, as they are anagram of each other.
"""

from itertools import permutations
def appearanceCount(len_code, len_msg, code, message):
    count = 0
    perm_code = [''.join(p) for p in permutations(code)]
    print perm_code
    print message
    for i in perm_code:
        if i in message:
            count = count + 1
            print i

    return count

code_size = int(raw_input())
msg_size = int(raw_input())
code = raw_input()
msg = raw_input()
print appearanceCount(code_size, msg_size, code, msg)
