def emergency ():
    active = True
    
    while (active):
        selection = 1
        if selection == 1: 
                
            scale = int(input("Welcome, from an scale of 0 to 10 ¿How do you describe your emergency?"))
            print (f'You have selected, {scale}.')
                
            if scale >= 0 and scale < 6:
                print ('Type I: Not consider an immediate threat, please wait for the doctor to be available for a regular office visit')
            elif scale >= 6 and scale < 9:
                print ('Type II: You received a preferencial turn, you will be in the first place of the waitlist')
            elif scale >= 9:
                print ('Type III: Inmediate turn, the vet is going to treat you right away')
            else:
                print('Type a valid option...')
                
emergency()
              
        