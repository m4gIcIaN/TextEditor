# Imports
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from webbrowser import open
from time import *

# Creating Text Editor Class
class TextEditor:

    global savedFile

# Creating the constructor function
    def __init__(self, master):

        # Initial Set-up
        master.title('Untitled')
        master.resizable(True, True)
        master.option_add('*tearOff', False)
        master.geometry('640x480+50+100')
        master.minsize(350,200)
        master.maxsize(1920,1080)

        # Creating the Menu on the top including all its branches
        topMenu = Menu(master)
        master.config(menu=topMenu)

        file = Menu(topMenu)
        edit = Menu(topMenu)
        format = Menu(topMenu)
        view = Menu(topMenu)
        help = Menu(topMenu)

        topMenu.add_cascade(menu=file, label='File')
        topMenu.add_cascade(menu=edit, label='Edit')
        topMenu.add_cascade(menu=format, label='Format')
        topMenu.add_cascade(menu=view, label='View')
        topMenu.add_cascade(menu=help, label='Help')

        file.add_command(label='New', accelerator='Ctrl+N')
        file.add_command(label='Open...', accelerator='Ctrl+O', command=lambda: self.openFile(textBox, master))
        file.add_command(label='Save', accelerator='Ctrl+S', command=lambda: self.save(textBox, master))
        file.add_command(label='Save As...', accelerator='', command=lambda: self.saveAs(textBox, master))
        file.add_separator()
        file.add_command(label='Page Setup...')
        file.add_command(label='Print...', accelerator='Ctrl+P')
        file.add_separator()
        file.add_command(label='Exit', command=lambda: exit())

        edit.add_command(label='Undo', accelerator='Ctrl+Z')
        edit.add_separator()
        edit.add_command(label='Cut', accelerator='Ctrl+X')
        edit.add_command(label='Copy', accelerator='Ctrl+C')
        edit.add_command(label='Paste', accelerator='Ctrl+V')
        edit.add_command(label='Delete', accelerator='Del')
        edit.add_separator()
        edit.add_command(label='Find...', accelerator='Ctrl+F')
        edit.add_command(label='Find Next', accelerator='F3')
        edit.add_command(label='Replace...', accelerator='Ctrl+H')
        edit.add_command(label='Go To...', accelerator='Ctrl+G')
        edit.add_separator()
        edit.add_command(label='Select All', accelerator='Ctrl+A')
        edit.add_command(label='Time/Date', accelerator='F5', command=lambda: self.printTimeDate(textBox))

        # Creates the Word Wrap's Functionality
        varWW = IntVar()
        format.add_checkbutton(label='Word Wrap', variable=varWW, command=lambda: self.checkWordWrap(varWW, textBox))
        format.add_command(label='Format...')

        # Creates the Status Bar's Functionality
        varSB = IntVar()
        view.add_checkbutton(label='Status Bar', variable=varSB, command=lambda: self.statusBarStatus(varSB, statusFrame))

        # Adds Help Buttons Functionality
        help.add_command(label='View Help', command=self.showHelp)
        help.add_separator()
        help.add_command(label='About TextEditor', command=self.showHelp)

        # Creates Text Area
        textBox = Text(master, wrap='none', font=14)

        # Creates Vertical and Horizontal Scroll Bar
        scrollVertical = ttk.Scrollbar(textBox, orient=VERTICAL, command=textBox.yview)
        scrollHorizontal = ttk.Scrollbar(textBox, orient=HORIZONTAL, command=textBox.xview)
        scrollVertical.pack(side=RIGHT, fill=Y)
        scrollHorizontal.pack(side=BOTTOM, fill=X)
        textBox.config(yscrollcommand=scrollVertical.set)
        textBox.config(xscrollcommand=scrollHorizontal.set)

        textBox.pack(fill=BOTH, expand=True)

        # Creates Status Bar 
        statusFrame = Label(text='Ln {}, Col {}'.format(textBox.get('0.0',INSERT), '4'))

        # Binds Keys to their respective functions
        master.bind('<Control-s>', lambda e: self.save(textBox, master))
        master.bind('<Control-o>', lambda e: self.openFile(textBox, master))
        master.bind('<F5>', lambda e: self.printTimeDate(textBox))

        # Loops Application
        master.mainloop()

    # Opens link to show Help
    def showHelp(self):
        open('https://learntocodewith.me/programming/basics/text-editors/', autoraise=True)

    # Checks if word wrap is on or off
    def checkWordWrap(self, var, text):
        if var.get() == 1:
            text.config(wrap='word')
        elif var.get() == 0:
            text.config(wrap='none')

    # Opens File
    def openFile(self, textBox, master):
        master.fileName = filedialog.askopenfile(initialdir='C:\\',
                                                 filetypes=(('Text Documents (*.txt)', '*.txt'), ('All Files', '*.*')),
                                                 title='Open File', mode='r')
        if master.fileName is None:
            return
        if master.fileName is not None:
            textBox.delete('1.0', END)
            master.title(master.fileName.name)
            textBox.insert(END, master.fileName.read())

    # Saves Files, Creates a new file
    def saveAs(self, textBox, master):
        global savedFile
        savedFile = filedialog.asksaveasfile(mode='+w', defaultextension='.txt')
        if savedFile is None:
            return
        if savedFile is not None:
            master.title(savedFile.name)
            print(textBox.get('1.0', END), file=savedFile)

    # Saves current file, creates a new file if one does not already exist
    def save(self, textBox, master):
        if str(master.title()) == 'Untitled' or str(master.title()) is None:
            self.saveAs(textBox, master)
        else:
            global savedFile
            savedFile.seek(0)
            savedFile.truncate()
            print(textBox.get('1.0', END), file=savedFile)
            print(savedFile.name)

    # Exits Application
    def exit(self):
        SystemExit()
        
    # Checks the Status Bars 
    def statusBarStatus(self, variable, statusBar):
        if variable.get() == 1:
            statusBar.pack()
        elif variable.get() == 0:
            statusBar.pack_forget()

    # Prints the current time
    def printTimeDate(self, textBox):
        textBox.insert(INSERT, strftime('%I:%M %p %m/%d/%Y', localtime()))

# Runs the Text Editor
def main():
    root = Tk()
    TextEditor(root)

# Checks validity and runs main()
if __name__ == '__main__':
    main()