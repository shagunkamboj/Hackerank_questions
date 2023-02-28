#output = hACKERrANK.COM PRESENTS "pYTHONIST 2".
#*****************************method 1 ***************************
s = "HackerRank.com presents Pythonist 2"
empty_string = ""
for i in s:
    print(i)
    if i.isupper():
        empty_string += i.lower()
        
    else:
        empty_string += i.upper()
print(empty_string)


#**************************method 2 **********************
s = "HackerRank.com presents Pythonist 2"
print(s.swapcase())
        