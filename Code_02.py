l1 = int(input("Enter number : "))
l2 = input("Enter word : ")
l3 = input("Enter word : ")
l4 = input("Enter word : ")
l5 = input("Enter word : ")
l6 = input("Enter word : ")

my_list = ['old', 'new', 'existing', 'new', 'new', 'old']

for item in sorted(set(my_list)):

    count = my_list.count(item)
    print(
       f'{item} = {count} times'
    )