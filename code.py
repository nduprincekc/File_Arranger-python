import shutil
import os
import webbrowser
from tkinter import messagebox,filedialog
from tkinter import *

root = Tk()
root.geometry("333x344+500+100")
root.title('File Arranger')
root.resizable(0,0)
root.config(bg='purple')
root.iconbitmap(r'folder.ico')


def link(e):
    webbrowser.open(e)


def arranger():
    try:
        path = l.get()
        files = os.listdir(path)

        for file in files:
            files,extension = os.path.splitext(file)
            extension = extension[1:]
            if os.path.exists(path+ '/' + extension):
                shutil.move(path+ '/' + file,path+'/'+extension+'/'+file)
            else:
                os.makedirs(path+'/'+extension)
                shutil.move(path + '/' + file, path + '/' + extension)

    except FileNotFoundError:
        messagebox.showerror('No Folder', 'Select a folder')


def open():
    f= filedialog.askdirectory()
    t1.set(f)


t1 = StringVar()
Label(root,text= 'File Arranger',width=22,font='arial 12 bold').pack()

# image icon
icon1 = PhotoImage(file= 'fileeeee.png')
icon2 = PhotoImage(file ='Untitledew.png')
icon3 = PhotoImage(file ='img_2.png')
l = Entry(root,textvariable= t1,width=44,state='disabled')
l.pack(padx=51)

open = Button(root,text='Select the File directory',width=231,height = 50,image = icon1,compound= RIGHT,command=open).place(x=50,y=120)


Arrange = Button(root,text='Arrange this File directory',width=231,height = 50,image = icon2,compound= RIGHT,command=arranger).place(x=50,y=51)


# close button
close = Button(root,text='Close ',width=231,height = 50,image = icon3,compound= RIGHT,command=root.destroy).place(x=50,y=201)

# My Github link
url=Label(root,text='Developed by Nduprincekc',cursor='hand2')
url.place(x=70,y=293)
url.bind('<Button-1>',lambda e:link('https://github.com/nduprincekc'))

root.mainloop()

