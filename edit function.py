def edit_field():
    def edit_button(new_name, new_id, address_new, phone_new, mail_new,
                    name, id_old, address_old, phone_old, mail_old):

        parameters_edit = (new_name, new_id, address_new, phone_new, mail_new,
                           name, id_old, address_old, phone_old, mail_old)

        run_query(query='UPDATE client SET name = ?, id_user = ?, address = ?, phone = ?, email = ? '
                        'WHERE name = ? AND id_user = ? AND address = ? AND phone = ? AND email = ?',
                  parameters=parameters_edit,
                  db=db_user)
        message['text'] = "UPDATE SUCCESSFULLY"
        edit_wind.destroy()

    message['text'] = ''
    try:
        management_windows.item(management_windows.selection())['text'][0]
    except IndexError as e:
        message['text'] = 'Please, select Record'
        return

    name = management_windows.item(management_windows.selection())['text']
    id_old = management_windows.item(management_windows.selection())['values'][1]
    address_old = management_windows.item(management_windows.selection())['values'][2]
    phone_old = management_windows.item(management_windows.selection())['values'][3]
    mail_old = management_windows.item(management_windows.selection())['values'][4]

    edit_wind = Toplevel()
    edit_wind.title = 'Edit Product'
    edit_wind.config(bg="white")

    # New Name
    Label(edit_wind, text='New Name:', bg="white").grid(row=1, column=1)
    new_name = Entry(edit_wind)
    new_name.insert(0, name)
    new_name.grid(row=1, column=2)

    # New ID
    Label(edit_wind, text='New ID Number:', bg="white").grid(row=2, column=1)
    new_id = Entry(edit_wind)
    new_id.insert(0, id_old)
    new_id.grid(row=2, column=2)

    # New address
    Label(edit_wind, text='New Address:', bg="white").grid(row=3, column=1)
    address_new = Entry(edit_wind)
    address_new.insert(0, address_old)
    address_new.grid(row=3, column=2)

    # New address
    Label(edit_wind, text='New Phone:', bg="white").grid(row=4, column=1)
    phone_new = Entry(edit_wind)
    phone_new.insert(0, phone_old)
    phone_new.grid(row=4, column=2)

    # New Email
    Label(edit_wind, text='New E-mail:', bg="white").grid(row=5, column=1)
    mail_new = Entry(edit_wind)
    mail_new.insert(0, mail_old)
    mail_new.grid(row=5, column=2)

    Button(edit_wind, text="UPDATE DATA", relief='ridge', bg="white",
           command=lambda: [edit_button(new_name.get(), new_id.get(), address_new.get(), phone_new.get(),
                                        mail_new.get(), name, id_old, address_old, phone_old, mail_old)]) \
        .grid(row=6, column=2, sticky="")


message = Label(text='', fg='red')
message.grid(row=6, column=3, columnspan=4, sticky="news")

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