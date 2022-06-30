
def menu():
        
    active = True
    while (active):
        choice = True
        while (choice):
                print ('== Menu Opciones ==')
                print ('1. Emergencia')
                print ('2. Vaunacion y desparacitación')
                print ('3. Baño y estetica')
                print ('4. Compra accesorios')
                print ('5. Salir')
                selection = int(input('Select an option from the menu: '))
                if selection >= 1 and selection <= 4:
                    choice = False
                    ejecutar(selection)
                elif selection == 5: 
                    active = False
                else: 
                    print ('Type a valid response...')
def ejecutar(selection):

    print (selection)

menu()


    
                        
    
            
