# def word_count(str):
#     counts = dict()
#     words = str.split()

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     return counts

# print( word_count('5 new old existing new new'))

from typing import overload


l1 = input("enter number : ")
l2 = input("enter word 2: ")
l3 = input("enter word 3: ")
l4 = input("enter word 4: ")
l5 = input("enter word 5: ")
l6 = input("enter word 6: ")

mywordlist = [len(l1), len(l2), len(l3), len(l4), len(l5), len(l6)]
print(mywordlist)



