def vacuna_parasito ():
    active = True
    while (active):
        selection = 3
        if selection == 3:
            deseo = str(input('What do you wanna do, vaccination or deworm?'))
            if deseo == 'vaccination':
                print (f'Perfect, you have selected {deseo}. ')
                print ('Place your pet in the table to take the vacciantion')
            elif deseo == 'deworm':
                print (f'Perfect, you have selected {deseo}. ')
                print ('Place your pet in the table to take the dewormer')
vacuna_parasito()
                