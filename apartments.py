import sqlEditor as sql

wPrice = 9
ePrice = 0.58

print(f'1 - enter values for apartment A\n2 - enter values for apartment B\n3 - enter values for both apartments\n')
action = int(input('enter your choice: '))

if action == 1:
    sql.addVal('apartment_a', wPrice, ePrice)
elif action == 2:
    sql.addVal('apartment_b',wPrice, ePrice)
elif action == 3:
    print("enter for A ")
    sql.addVal('apartment_a', wPrice, ePrice)
    print("enter for B ")
    sql.addVal('apartment_b', wPrice, ePrice)
else:
    print("invalid input!!!!!!")
