
'''Count the no. 4 in a given list'''

len = int(input ("please enter your list lenght: "))
my_list=[]
for _ in range(len):
    temp = int(input ("enter list item: "))
    my_list.append(temp)

four_count=my_list.count(4)
print("number 4 occurs",four_count," times")