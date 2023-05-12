import re

s = '(2+ 3) *4 - 5 * 3'
s.replace(' ', '')
# print(s)

my_list = re.findall(r'\d+|[+\-*/()]', s)
print(my_list)

# t = []
# w = ''
# q = []

# for i in s:
#     t.append(i)
# print(t)

# my ['', '(', '2', '+', '3', ')', '', '*', '4', '-', '5', '*', '3']
# nm  ['(', '2', '+', '3', ')', '*', '4', '-', '5', '*', '3']