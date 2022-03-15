import random
from tkinter import *
from tkinter import ttk

# Create an instance of Tkinter frame
win = Tk()
win.title("Kódosítás")

# Set the geometry of Tkinter frame
win.geometry("670x200")



def display_text():
    global entry
    string = entry.get()
    if len(string) < 6:
        label.configure(text="6 karakternél hosszabb jelszó szükséges")
    else:
        label.configure(text=encrypt(string))

def encrypt(string):
    string = sorted(string)
    kapcsolo = False
    k = 1
    for i in range(len(string)):
        randomNum = random.randint(1,6)
        if i == (len(string)-1):
            kapcsolo = True
        if kapcsolo == False:
            string[k] = str(randomNum)
            if (k+2) < len(string):
                k += 2
        else:
            utso = str(len(string))
    lista = ["1", "2", "3", "4", "5", "6",]
    for i,elem in enumerate(string):
        if elem in lista:
            if int(elem) % 2 == 0:
                string[i] = string[random.randint(0, len(string)-1)]
            else:
                string[i] = str(random.randint(22, 63))
    string += utso
    return string


# Initialize a Label to display the User Input
label = Label(win, text="", font=("Courier 22 bold"), bg="yellow")
label.pack()

# Create an Entry widget to accept User Input
entry = Entry(win, width=25, bg="white", fg="black")
entry.focus_set()
entry.pack()

# Create a Button to validate Entry Widget
ttk.Button(win, text="Encrypt", width=20, command=display_text, cursor="pirate").pack(pady=1)
print("aadada")
win.mainloop()
