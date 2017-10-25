"""

Here a interview is going on. The interview is rating the candidates based on their performance, but he is pissed of this job. So whenever a candidate scores 0 mark, he removes the candidate from
the list, along with it he removes the immediate previous candidate and his score as well. In the end interview has to find the average score of all the candidates.
Following is the code.

Input will be the number of candidates, and their scores.

"""
limit = int(raw_input())
new_val = 0
previous_val = 0

for i in xrange(limit):

    val = int(raw_input())

    if val == 0:
        new_val = new_val - previous_val
        
    else:
        new_val = new_val+val
        previous_val = val
        

print float(new_val)/float(limit)
