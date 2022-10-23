from tkinter import *
import subprocess, sys

# powershell functions / powershell part
def Create_VM():
    p = subprocess.Popen(["powershell.exe", "C:\Learning\Powershell\Other\Create_VM.ps1"],stdout=sys.stdout)
    p.communicate()
def Hello_World():
    p = subprocess.Popen(["powershell.exe", "C:\Learning\Powershell\Other\script.ps1"],stdout=sys.stdout)
    p.communicate()
def justaotherpowershellscript():
    p = subprocess.Popen(["powershell.exe", "C:\Learning\Powershell\Other\justaotherpowershellscript.ps1"],stdout=sys.stdout)
    p.communicate()


# Object
Manager = Tk()

Manager.title('Script Manager')
Manager.geometry('800x400')

# Example how to add text
# Script1 = Label(Manager, text='Create VM')
# Script1.grid(column=1,row=0)

Button1 = Button(Manager, text = 'Click Here to create vm',bg='aqua',fg='black',command=Create_VM)
Button1.grid(column=1,row=1)

Button1 = Button(Manager, text = 'Last Script',bg='aqua',fg='black',command=Hello_World)
Button1.grid(column=2,row=1)

Button1 = Button(Manager, text = 'Another Script',bg='aqua',fg='black',command=justaotherpowershellscript)
Button1.grid(column=3,row=1)




# Line below starts program
Manager.mainloop()


