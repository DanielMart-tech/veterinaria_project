def shower_stetic ():
    active = True
    while (active):
        selection =2
        if selection == 2:
            deseo = str(input('Do you want to give your pet a bath?'))
            if deseo == 'yes':
                print (f'Perfect, you have said {deseo}. ')
                print ('Place your pet in the table to take the bath')
                choice_1 = str(input('Besides the bath, do you want a stetic procedure?: '))
                
                if choice_1 == 'yes':
            
                    print ('Perfect, which other stetic procedure do you want?')
                    print ("=== Stetic procedures ===\n\1- Cut nails.\n\2- Cut Hair.\n\3- Paint Nails.\n\4- Finish Service.")
                    choice_3= int (input(': '))
                    print (f'You have selected {choice_3}')
                              
            elif deseo == 'no':
                print(f'Okay, thank you for using our services.')
                active = False
shower_stetic()