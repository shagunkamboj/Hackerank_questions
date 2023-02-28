'''Given the participants' score sheet for your University Sports Day, you are required to
find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
Explanation 0
Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.'''
l = [2 ,3, 6 ,6, 5]
convert_to_set = set(l)
maximum = max(convert_to_set)
empty_list = []
for i in convert_to_set:
    if i != maximum:
        empty_list.append(i)
print(max(empty_list))