"""
Input will be the number of anagram, and the list of anagrams. We have to find the number of anagram that appears the highest time.

"""

data = []
size_list = []
limit = int(raw_input())

for i in range(limit):
    val = raw_input()
    data.append(val)
    
for i in data:
    size = len(i)
    size_list.append(size)
    

val_new = max(size_list,key=size_list.count)
print val_new
