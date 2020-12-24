import sys

first_list = sys.argv[1]
second_list = sys.argv[2]

# odds = [x for  x in first_list if x % 2 != 0]
# evens = [x for  x in second_list if x % 2 == 0]
# joined_list = odds + evens

joined_list = []
for x in first_list:
    if x % 2 != 0:
        joined_list.append(i)
for x in second_list:
    if x % 2 == 0:
        joined_list.append(x)
print(joined_list)
