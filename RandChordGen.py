#This application generates a random maj/min chord wit +7 or +9.
#TODO: remove dirty marks left by previous chords
import tkinter as tk
import random 

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 200, height = 150)
root.title("Random Chord Generator")

canvas1.pack()

def GenerateRandomChord():
    #get a note
    Noteset = ["do","re","mi","fa","sol","la","si","do#","re#","fa#","sol#","la#"]
    note = random.choice(Noteset)
    #get a maj/min
    Tonalities = ["maj","min"] #,"dim","half dim","aug"
    tonality = random.choice(Tonalities) 
    #get none/+7/+9
    Additionals = [" ","+7","+9"] #,"+7+9"
    add = random.choice(Additionals)

    return str(note+" "+tonality+" "+add)

def printer (): 
    label1 = tk.Label(root, text= GenerateRandomChord(), fg='black', font=('helvetica', 12, 'bold'))
    canvas1.create_window(100, 100, window=label1)

button1 = tk.Button(text='Generate Chord',command=printer, bg='brown',fg='white')
canvas1.create_window(100, 50, window=button1)
labelcred = tk.Label(root, text= "made by Keral", fg='black', font=('helvetica', 5))
canvas1.create_window(30, 140, window=labelcred)

root.mainloop()