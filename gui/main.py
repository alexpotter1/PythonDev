# test GUI program, Alex Potter

# functions!

def errorTK():
    print("Tkinter not installed!")

def pinger(ip): # pings ip address
    import subprocess
    import re
    global output1
    output1 = "Pinging %s" % ip
    return output1

    CMD = ['ping', '-c', '1', '%s' % ip]
    result = subprocess.check_output(CMD) # gets ping
    global output2
    output2 = "%s is up!" % ip
    return output2
        
            
                 
 
    #global output3
    #output3 = "%s didn't respond." % ip # these need to be displayed by print/labelVariable.set()
    #return output3




try:
    import tkinter
except ImportError:
    errorTK()
else:
    print("Tkinter detected!")
    pass

class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent): # Tkinter constructor
        tkinter.Tk.__init__(self,parent) # same
        self.parent = parent # parent ref
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

        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable,anchor='sw',fg="white",bg="darkgrey") # text label, anchored to west side of program window
        label.grid(column=0,row=1,columnspan=2,
                   sticky='SWE')
        self.labelVariable.set("Hello!")

        self.grid_columnconfigure(0,weight=1) # use this to allow resizing of objects
        self.update()
        self.geometry(self.geometry())

    def OnButtonClick(self):
        import time
        pingVar = self.textentryVariable.get()
        pinger(pingVar)
        self.labelVariable.set(output1)
        time.sleep(5)
        self.labelVariable.set(output2)

        self.labelVariable.set(output3)

        
        

    def OnPressEnter(self, event): # this adds an extra event arg, probably because of enter
       pingVar = self.textentryVariable.get()
       pinger(pingVar)
       self.labelVariable.set(output1)
       try:
           self.labelVariable.set(output2)
       except:
           pass
       try:
           self.labelVariable.set(output3)
       except:
           pass
        



if __name__ == "__main__":
    app = simpleapp_tk(None) # no parent!
    app.title("Socket Program")
    app.mainloop() # makes sure program loops + waits for input
