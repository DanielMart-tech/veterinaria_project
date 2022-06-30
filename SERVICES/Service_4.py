def accesories():
    active = True
    while (active):
        selection =4
        if selection == 4: 
            print ('Thank you for shopping with us today.')
            print ('These are our products ¿Which one do you want?')
            print ("=== Stetic procedures ===\n\
1- Plastic ball.\n\
2- Freesbe.\n\
3- Bone.\n\
4- Teddy bear.\n\
5- Exit")
            select = int(input('= '))
            if select == 1:
                print ('You have selected, plastic ball. you´ll see an extra charge on the bill for the cost of the item')
            elif select == 2:
                print ('You have selected, freesbe. you´ll see an extra charge on the bill for the cost of the item')
            elif select == 3:
                print ('You have selected, bone. you´ll see an extra charge on the bill for the cost of the item ')
            elif select == 4:
                print ('You have selected, teddy bear. you´ll see an extra charge on the bill for the cost of the item')
            elif select == 5:
                print ('Thanks for using our services! good bye!')
                break
            else:
                print ('select a valid option...')
            
accesories()