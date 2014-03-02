# test GUI program, Alex Potter

# functions!

import sys

try:
    import APIs
except ImportError:
    print("Oops, something went wrong with the API module!")
else:
    pass

try:
    import tkinter
except ImportError:
    print("Tkinter not installed/detected!")
else:
    print("Tkinter detected!")
    pass



class simpleapp_tk(tkinter.Tk):
    counter = 1
    def __init__(self,root): # Tkinter constructor
        tkinter.Tk.__init__(self,root) # same
        self.parent = root # parent ref
        self.initialise() # calling init of window

    def initialise(self): # code goes here
        self.grid() # setting up grid manager for objs

        self.textentryVariable = tkinter.StringVar() # making new text entry variable
        self.textentry = tkinter.Entry(self, textvariable=self.textentryVariable) # adding textentry
        self.textentry.grid(column=0,row=0,sticky='EW') # setting location + stick to east + west of window
        self.textentry.bind("<Return>",self.OnPressEnter) # binds the entry field to the return button, and then launches event handler
        self.textentryVariable.set("Enter a URL/IP address here...") # setting text entry var
        

        button = tkinter.Button(self,text="Ping!",command=self.OnButtonClick) # creating button to confirm entry + location params, binds button to evt handler
        button.grid(column=1,row=0) # call everything with window manager (in this case, grid())

        button2 = tkinter.Button(self,text="Settings",command=self.OnSettingButtonClick)
        button2.grid(column=2,row=0)

        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable,anchor='sw',fg="white",bg="darkgrey") # text label, anchored to west side of program window
        label.grid(column=0,row=1,columnspan=3,
                   sticky='SWE')
        self.labelVariable.set("Hello!")
        sys.stdout = self

        self.grid_columnconfigure(0,weight=1) # use this to allow resizing of objects
        self.update()
        self.minsize(500,300)
        self.geometry("700x400")

    def OnButtonClick(self):
        pingVar = self.textentryVariable.get()
        APIs.pinger(pingVar)
        self.labelVariable.set(APIs.ping_first)
        if APIs.errorout:
            self.labelVariable.set(APIs.errorout)
        else:
            self.labelVariable.set(APIs.output)

    def OnSettingButtonClick(self):
        self.counter += 1 # just a little counter so I know how many windows there are running ;)
        self.child=tkinter.Toplevel(master=self.parent) # creates a new instance of self (child) and sets it to create a new window which is a child of 'root' (self.parent)

        self.child.labelSettingsVariable = tkinter.StringVar()
        child_button = tkinter.Button(self.child,text="TEST",command="OnClickTest")
        child_button.grid(column=0,row=0)

        self.child.grid_columnconfigure(0,weight=1)
        self.child.update()
        self.child.geometry(self.child.geometry())

        def OnClickTest(self):
            pass

        

    def OnPressEnter(self, event): # this adds an extra event arg, probably because of enter
       pingVar = self.textentryVariable.get()
       APIs.pinger(pingVar)
       self.labelVariable.set(APIs.ping_first)
       if APIs.errorout:
           self.labelVariable.set(APIs.errorout)
       else:
           self.labelVariable.set(APIs.output)

        



if __name__ == "__main__":
    app = simpleapp_tk(None) # no parent!
    app.title("Socket Program")
    app.mainloop() # makes sure program loops + waits for input
