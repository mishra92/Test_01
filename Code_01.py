# # define a function named as prog and name of parameter is "le"
# def prog(le):
# # with type method we check what type of datatype, (le) is holding
#     if type(le) is list:
#         print("List Length : ",len(le)) 
#         print("List Elements...")
#         # If (le) is List, checking its Length.
#         for i in le:
#             print(i)
# # if type (le) is str:
#     print("String Length : ",len(le))
#     print("String Characters...")
#     for i in le:
#         print(i,end='')
# l1 = int(input("Enter Number : "))
# l2 = input("Enter Word : ")
# l3 = input("Enter Word : ")
# l4 = input("Enter Word : ")
# l5 = input("Enter Word : ")
# list1=[l1, l2, l3, l4, l5]
# prog(list1)

def list_word(Word):
    word_len = []
    for n in Word:
        word_len.sort((len(n), n))
        word_len.__len__()
        return word_len[0]

print(list_word(["old", "new", "new", "existing", "new"]))

