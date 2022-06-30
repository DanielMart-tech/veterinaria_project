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
                    print ("=== Stetic procedures ===\n\
1- Cut nails.\n\
2- Cut Hair.\n\
3- Paint Nails.\n\
4- Finish Service.")
                    choice_3= int (input(': '))
                    if choice_3 == 1:
                        print ('You have selected, cut nails.')
                        
                    elif choice_3 == 2:
                        print ('You have selected, cut hair.')
                        
                    elif choice_3 == 3:
                        print ('You have selected, pait nails.')
                        
                    elif choice_3 == 4:
                        print ('Okay, thanks for coming today!')
                        break
                    else:
                        print ('Select a correct option...') 
                        
                              
            elif deseo == 'no':
                print('Okay, thank you for using our services.')
                active = False
            else: 
                print ('Enter a valid option...')
shower_stetic()