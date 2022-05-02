import tkinter
import tkinter as tk  # import tkinter
from datetime import datetime
from tkinter import ttk, messagebox
from csv import DictWriter
import os
import re

win = tk.Tk()
win.title('Quick Question Survey')

counter = 00


def counter_label(label):
    counter = 00

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()


Label = tk.Label(win, background="Green", width=10, height=3, text="Time: ", font='Verdana', foreground='Black')
Label.grid(row=1, column=5)
counter_label(Label)

Owner_Labe = tk.Label(win, text="Made with ❤ hosted Akshat Sanvaliya")
Owner_Labe.grid(row=27, column=5)
# create labels
# name label
name_label = ttk.Label(win, text="Enter Your Name : ")
name_label.grid(row=0, column=0, sticky=tk.W)

# email label
email_label = ttk.Label(win, text="Enter Your Email : ")
email_label.grid(row=1, column=0, sticky=tk.W)

# age label
age_label = ttk.Label(win, text="Enter Your Age : ")
age_label.grid(row=2, column=0, sticky=tk.W)

# mobile number label
mobile_label = ttk.Label(win, text="Enter Your Mobile Number : ")
mobile_label.grid(row=3, column=0, sticky=tk.W)
gender_label = ttk.Label(win, text="Select your Gender: ")
gender_label.grid(row=4, column=0, sticky=tk.W)
# gender label
Ques1 = ttk.Label(win, text="Q1. Raw data should be processed only one time. ")
Ques1.grid(row=6, column=0, sticky=tk.W)

Ques2 = ttk.Label(win, text="Q2.Which among the following is the top most important thing in DS ")
Ques2.grid(row=7, column=0, sticky=tk.W)

Ques3 = ttk.Label(win, text="Q3.  Which approach should be used if you can’t fix the variable?")
Ques3.grid(row=8, column=0, sticky=tk.W)

Ques4 = ttk.Label(win, text="Q4.  _________ is a good way of performing experiments in data science")
Ques4.grid(row=9, column=0, sticky=tk.W)

Ques5 = ttk.Label(win, text="Q5.   A data scientist is a job title for an employee or business intelligence ("
                            "BI) consultant who excels at analyzing data, particularly large amounts of data.")
Ques5.grid(row=10, column=0, sticky=tk.W)

# Create entry box
# name entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=16, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

# email entry box
email_var = tk.StringVar()

email_entrybox = ttk.Entry(win, width=16, textvariable=email_var)

email_entrybox.grid(row=1, column=1)

# age entry box
age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=16, textvariable=age_var)
age_entrybox.grid(row=2, column=1)

# mobile entry box
mobile_var = tk.StringVar()
mobile_entrybox = ttk.Entry(win, width=16, textvariable=mobile_var)
mobile_entrybox.grid(row=3, column=1)

# create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=13, textvariable=gender_var, state="readonly")
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.current(0)
gender_combobox.grid(row=4, column=1)

# Create radio button
Q1 = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text='True', value='True', variable=Q1, cursor="spider")
radiobtn1.grid(row=6, column=0)

radiobtn2 = ttk.Radiobutton(win, text='False', value='False', variable=Q1, cursor="clock")
radiobtn2.grid(row=6, column=1)



Q2 = tk.StringVar()
radiobtn3 = ttk.Radiobutton(win, text='Answer', value='Answer', variable=Q2, cursor="pirate")
radiobtn3.grid(row=7, column=0)
radiobtn10 = ttk.Radiobutton(win, text='Question', value='Question', variable=Q2, cursor="dotbox")
radiobtn10.grid(row=7, column=1)


Q3 = tk.StringVar()
radiobtn4 = ttk.Radiobutton(win, text='generalize it', value='generalize it', variable=Q3, cursor="spraycan")
radiobtn4.grid(row=8, column=0)
radiobtn5 = ttk.Radiobutton(win, text='randomize it', value='randomize it', variable=Q3, cursor="tcross")
radiobtn5.grid(row=8, column=1)


Q4 = tk.StringVar()
radiobtn6 = ttk.Radiobutton(win, text='variability', value='variability', variable=Q4, cursor="trek")
radiobtn6.grid(row=9, column=0)
radiobtn7 = ttk.Radiobutton(win, text='Verification', value='Verification', variable=Q4, cursor="watch")
radiobtn7.grid(row=9, column=1)


Q5 = tk.StringVar()
radiobtn8 = ttk.Radiobutton(win, text='False', value='False', variable=Q5, cursor="spider")
radiobtn8.grid(row=10, column=1)
radiobtn9 = ttk.Radiobutton(win, text='True', value='True', variable=Q5, cursor="spider")
radiobtn9.grid(row=10, column=2)


# create check button
checkbtn_var = tk.StringVar()
l6 = ttk.Label(win, text="       Satisfied with our survey?")
l6.grid(row=23, column=0, sticky=tk.W)
radiobtn10 = ttk.Radiobutton(win, text='Yes', value='Yes', variable=checkbtn_var, cursor="spider")
radiobtn10.grid(row=23, columnspan=1)
radiobtn11 = ttk.Radiobutton(win, text='No', value='No', variable=checkbtn_var, cursor="spider")
radiobtn11.grid(row=23, column=2)


# Create button code action function
def action():
    name = name_var.get()
    try:
        if name == '':
            tkinter.messagebox.showwarning('', 'Please fill all the required fields')
            return
        if name.isdigit():
            raise NameError
    except NameError:
        tkinter.messagebox.showerror('Error', 'Your name should only comprise of characters!')
        return

    e = email_entrybox.get()
    try:
        if e == '':
            tkinter.messagebox.showwarning('', 'Please fill all the required fields')
            return
        l5 = e.split('@')
        if len(l5) != 2:
            raise IndexError
        l6 = l5[1].split('.')
        if len(l6) != 2:
            raise IndexError
    except IndexError:
        tkinter.messagebox.showerror('Error', 'Enter valid Email id!')
        return

    m = mobile_entrybox.get()  # '''mobile no.'''
    try:
        if (m == ''):
            tkinter.messagebox.showwarning('', 'Please fill all the required fields')
            return
        if (m.isdigit() == False):
            raise ValueError
        if (len(m) != 10):
            raise ValueError
    except ValueError:
        tkinter.messagebox.showerror('Error', 'Phone number should only have 10 digits!')
        return

    a = age_entrybox.get()  # '''day'''
    try:
        if (a == ''):
            tkinter.messagebox.showwarning('', 'Please fill all the required fields')
            return
        if (a.isnumeric() == False):
            raise ValueError
    except ValueError:
        tkinter.messagebox.showerror('Error', 'Enter valid Age!')
        return

    username = name_var.get()
    userage = age_var.get()
    useremail = email_var.get()
    usermobile = mobile_var.get()
    usergender = gender_var.get()
    usertype = Q1.get()
    Q_2 = Q2.get()
    Q_3 = Q3.get()
    Q_4 = Q4.get()
    Q_5 = Q5.get()
    # change value 0,1 to Yes or No
    rad = checkbtn_var.get()

    # write to csv file code here
    with open('file.csv', 'a', newline='') as f:
        dict_writer = DictWriter(f,
                                 fieldnames=['User Name', 'User Age', 'User Email', 'User Mobile', 'User Gender',
                                             'User Type', 'Q2', 'Q3', 'Q4', 'Q5', 'Satisfy', 'Time'])
        if os.stat('file.csv').st_size == 0:  # if file is not emptier than header write else not
            dict_writer.writeheader()

        dict_writer.writerow({
            'User Name': username,
            'User Age': userage,
            'User Email': useremail,
            'User Mobile': usermobile,
            'User Gender': usergender,
            'User Type': usertype,
            'Q2': Q_2,
            'Q3': Q_3,
            'Q4': Q_4,
            'Q5': Q_5,
            'Satisfy': rad,
            'Time': counter
        })
    # Change color after submit button
    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    mobile_entrybox.delete(0, tk.END)
    name_label.configure(foreground='Blue')
    email_label.configure(foreground='Blue')
    age_label.configure(foreground='Blue')
    mobile_label.configure(foreground='Blue')
    Ques1.configure(foreground='Blue')
    Ques2.configure(foreground='Blue')
    Ques3.configure(foreground='Blue')
    Ques4.configure(foreground='Blue')
    Ques5.configure(foreground='Blue')


# submit button
submit_button = ttk.Button(win, text="Submit", command=action)
submit_button.grid(row=26, column=0)

win.mainloop()  # application is not closed auto
