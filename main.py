import sqlite3
from tkinter import ttk
from tkinter import *
from client import Client
from animal import Animal

db_user = "database.db"
db_animal = "animaldb.db"


def run_query(query, parameters=(), db=None):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result


def animal_register():
    def animal_data():
        species_data = str(animal_species.get()).title()
        animal_name_data = str(animal_name.get()).title()
        animal_age_data = int(animal_age.get())
        animal_weight_data = float(animal_weight.get())
        animal_height_data = float(animal_height.get())
        animal_illness_data = str(animal_illness.get()).title()
        Animal(species_data, animal_name_data, animal_age_data, animal_weight_data, animal_height_data,
               animal_illness_data)

        run_query(query="INSERT INTO animal VALUES(NULL, ?, ?, ?, ?, ?, ?)",
                  parameters=(species_data, animal_name_data, animal_age_data, animal_weight_data, animal_height_data,
                              animal_illness_data), db=db_animal)

    window_animal = Toplevel(window)
    window_animal.config(bg="white")
    window_animal.title("Veterinary User Registration")
    frame_animal = LabelFrame(window_animal, text="Pet Registration", bg="white")
    frame_animal.grid(row=0, column=0, columnspan=3, pady=20, padx=15)

    animal_species = StringVar()
    animal_name = StringVar()
    animal_age = StringVar()
    animal_weight = StringVar()
    animal_height = StringVar()
    animal_illness = StringVar()

    Label(frame_animal, text="Pet Species: ", bg="white").grid(row=1, column=0)
    animal_label = Entry(frame_animal, textvariable=animal_species)
    animal_label.focus()
    animal_label.grid(row=1, column=1, pady=5, padx=5)

    Label(frame_animal, text="Pet Name: ", bg="white").grid(row=2, column=0)
    animal_name = Entry(frame_animal, textvariable=animal_name)
    animal_name.grid(row=2, column=1, pady=5, padx=5)

    Label(frame_animal, text="Pet Age ", bg="white").grid(row=3, column=0)
    pet_age = Entry(frame_animal, textvariable=animal_age)
    pet_age.grid(row=3, column=1, pady=5, padx=5)

    Label(frame_animal, text="Pet Weight (Kg) : ", bg="white").grid(row=4, column=0)
    pet_weight = Entry(frame_animal, textvariable=animal_weight)
    pet_weight.grid(row=4, column=1, pady=5, padx=5)

    Label(frame_animal, text="Pet Height (cm) : ", bg="white").grid(row=5, column=0)
    pet_height = Entry(frame_animal, textvariable=animal_height)
    pet_height.grid(row=5, column=1, pady=5, padx=5)

    Label(frame_animal, text="Pet Illness: ", bg="white").grid(row=6, column=0)
    pet_illness = Entry(frame_animal, textvariable=animal_illness)
    pet_illness.grid(row=6, column=1, pady=5, padx=5)

    Button(frame_animal, text="Save Pet Data", relief='ridge', bg="white",
           command=lambda: [animal_data(), window_animal.destroy()]).grid(row=7, columnspan=3, pady=5)

    Button(frame_animal, text="Quit Window", relief='ridge', bg="white",
           command=lambda: window_animal.destroy()).grid(row=8, columnspan=3, pady=5)

    window_animal.mainloop()


def user_register():
    def client_data():
        user_data = str(user_name.get()).title()
        id_data = int(user_id.get())
        address_data = str(user_address.get()).title()
        phone_data = str(user_phone_number.get())
        mail_data = str(user_email.get()).lower()
        Client(user_data, id_data, address_data, phone_data, mail_data)

        run_query(query="INSERT INTO client VALUES(NULL, ?, ?, ?, ?, ?)",
                  parameters=(user_data, id_data, address_data, phone_data, mail_data), db=db_user)

    window_user = Toplevel(window)
    window_user.title("Veterinary Clinic Control")
    window_user.config(bg="white")
    frame_user = LabelFrame(window_user, text="Customer Register", font=("Bold", 12), bg="white")
    frame_user.grid(row=0, column=0, columnspan=3, pady=20, padx=15)

    user_name = StringVar()
    user_id = StringVar()
    user_address = StringVar()
    user_phone_number = StringVar()
    user_email = StringVar()

    Label(frame_user, text="Name: ", bg="white").grid(row=1, column=0)
    name_label = Entry(frame_user, textvariable=user_name)
    name_label.focus()
    name_label.grid(row=1, column=1, pady=5, padx=5)

    Label(frame_user, text="Id Number: ", bg="white").grid(row=2, column=0)
    id_client_label = Entry(frame_user, textvariable=user_id)
    id_client_label.grid(row=2, column=1, pady=5, padx=5)

    Label(frame_user, text="Address: ", bg="white").grid(row=3, column=0)
    address_label = Entry(frame_user, textvariable=user_address)
    address_label.grid(row=3, column=1, pady=5, padx=5)

    Label(frame_user, text="Phone Number: ", bg="white").grid(row=4, column=0)
    phone_label = Entry(frame_user, textvariable=user_phone_number)
    phone_label.grid(row=4, column=1, pady=5, padx=5)

    Label(frame_user, text="E-mail: ", bg="white").grid(row=5, column=0)
    mail_label = Entry(frame_user, textvariable=user_email)
    mail_label.grid(row=5, column=1, pady=5, padx=5)

    Button(frame_user, text=" Save Customer Data", bg="white", relief='ridge',
           command=lambda: [client_data(), window_user.destroy(), animal_register()]) \
        .grid(row=6, columnspan=3, pady=5)
    Button(frame_user, text="Quit Window", bg="white", relief='ridge',
           command=lambda: window_user.destroy()).grid(row=7, columnspan=3, pady=5)

    get_info_client()
    window_user.mainloop()


def get_info_client():
    def delete_field():
        message['text'] = ''
        try:
            management_windows.item(management_windows.selection())['text'][0]
        except IndexError as e:
            message['text'] = 'PLEASE SELECT A RECORD'
            return
        message['text'] = ''
        name = management_windows.item(management_windows.selection())['text']
        query_delete = 'DELETE FROM client WHERE name = ?'
        run_query(query=query_delete, parameters=(name, ), db=db_user)
        message['text'] = 'Record {} deleted Successfully'.format(name)
        get_info_client()

    def edit_field():
        message['text'] = ''
        try:
            management_windows.item(management_windows.selection())['text'][0]
        except IndexError as e:
            message['text'] = 'Please, select Record'
            return

        name = management_windows.item(management_windows.selection())['text']
        old_name = management_windows.item(management_windows.selection())['values'][1]
        edit_wind = Toplevel()
        edit_wind.title = 'Edit Product'

        # Old Name
        Label(edit_wind, text='Old Name:').grid(row=0, column=1)
        Entry(edit_wind, textvariable=StringVar(edit_wind, value=name), state='readonly').grid(row=0, column=2)

        # New Name
        Label(edit_wind, text='New Name:').grid(row=1, column=1)
        new_name = Entry(edit_wind)
        new_name.grid(row=1, column=2)

        # Old ID
        Label(edit_wind, text='Old ID:').grid(row=3, column=1)
        Entry(edit_wind, textvariable=StringVar(edit_wind, value=id_user), state='readonly').grid(row=0, column=2)

        # New ID
        Label(edit_wind, text='New Name:').grid(row=1, column=1)
        new_id = Entry(edit_wind)
        new_id.grid(row=1, column=2)

    message = Label(text='', fg='red')
    message.grid(row=6, column=4, columnspan=2, sticky=W + E)

    management_windows = ttk.Treeview(
        columns=("Name", "Identification", "Address", "Phone Number", "E-mail"),
        selectmode="extended",
        show="headings",
    )
    management_windows.grid(row=5, column=0, columnspan=10)
    management_windows.heading("#1", text="Name", anchor=CENTER)
    management_windows.column("#1", stretch=YES, minwidth=50, width=140)
    management_windows.heading("#2", text="Identification", anchor=CENTER)
    management_windows.column("#2", stretch=YES, minwidth=50, width=80)
    management_windows.heading("#3", text="Address", anchor=CENTER)
    management_windows.column("#3", stretch=YES, minwidth=50, width=200)
    management_windows.heading("#4", text="Phone Number", anchor=CENTER)
    management_windows.column("#4", stretch=YES, minwidth=50, width=100)
    management_windows.heading("#5", text="E-mail", anchor=CENTER)
    management_windows.column("#5", stretch=YES, minwidth=50, width=140)

    Button(text="DELETE USER", relief='ridge', bg="white", command=delete_field).grid(row=6, column=0, sticky="w")
    Button(text="EDIT USER", relief='ridge', bg="white", command=edit_field).grid(row=6, column=9, sticky="nesw")

    message = Label(text='', fg='red')
    message.grid(row=6, column=2, columnspan=2, sticky="w")

    scroll = ttk.Scrollbar(management_windows, orient="vertical")
    scroll.place(x=645, y=18, height=207)

    query = "SELECT * FROM client ORDER BY name DESC"
    db_rows = run_query(query, db=db_user)
    for row in db_rows:
        management_windows.insert("", "0", text=row[1], values=(row[1], row[2], row[3], row[4], row[5]))


window = Tk()

canvas = Canvas(width=400, height=300, bg="white")
canvas_image = PhotoImage(file="images/vet.png")
canvas_front = canvas.create_image(100, 50, image=canvas_image)
canvas.grid(row=0, column=0, columnspan=4)


window.title("Veterinary Clinic Control")
window.resizable(width=False, height=False)
frame = LabelFrame(window, text="MAIN MENU", font=("Bold", 15), bg="white", bd=0)
frame.grid(row=0, column=0, columnspan=4, pady=20, padx=20, sticky="")

#
user_register_button = Button(frame, text="Customer Register", command=user_register, relief='ridge', bg="white", ) \
    .grid(row=1, columnspan=3, pady=5, sticky="nesw")

services_button = Button(frame, text="Customer Services", relief='ridge', bg="white", ) \
    .grid(row=2, columnspan=3, pady=5, sticky="nesw")

user_management_button = Button(frame, text="User Management", relief='ridge', bg="white",
                                command=get_info_client) \
    .grid(row=3, columnspan=3, pady=5, sticky="nesw")

exit_button = Button(frame, text="Quit Program", relief='ridge', bg="white",
                     command=lambda: window.destroy()) \
    .grid(row=4, columnspan=3, pady=5, sticky="nesw")

window.mainloop()
