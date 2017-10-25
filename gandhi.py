"""
The mirror number. We give an input, and we have to place the number in the mirror and check whether the input is same as the output.
Example: 101 | 101
In 020 the output will be reverse.

"""


val_list = []
rev_list =[]
result = []
limit = int(raw_input())
for i in range(limit):
    temp = int(raw_input())
    sss = str(temp)
    if "2" in sss or "3" in sss or "4" in sss or "5" in sss or "6" in sss or "7" in sss or "9" in sss:
        pass
    elif "1" in sss or "0" in sss or "8" in sss:
        val_list.append(sss)

for j in val_list:
    rev_str = j[::-1]
    rev_list.append(rev_str)


for i in val_list:
    for j in rev_list:
        if i == j:
            result.append("Yes")
        else:
            result.append("No")
print set(result)
print result
for k in set(result):
    print k
