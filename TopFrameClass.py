import tkinter as tk
from tkinter import messagebox
from ParameterFrameClass import ParameterFrameClass
class TopFrameClass:

    def buildFrame(self,fatherFrame, client):
        self.client = client
        self.TopFrame = tk.LabelFrame(fatherFrame, text='Top')
        self.TopFrame.pack(fill="both", expand="yes", padx=10, pady=5)

        self.TopFrame.rowconfigure(0, weight=1)  # weight=1 -> va a tener el mismo tamaño que lo que tenga en la fila 1
        self.TopFrame.rowconfigure(1, weight=1)
        self.TopFrame.rowconfigure(2, weight=1)
        self.TopFrame.columnconfigure(0, weight=1)
        self.TopFrame.columnconfigure(1, weight=1)
        self.TopFrame.columnconfigure(2, weight=1)
        self.TopFrame.columnconfigure(3, weight=1)

        self.Button1 = tk.Button(self.TopFrame, text="Show alert", bg='red', fg="white", command=self.button1Clicked)
        self.Button1.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")  # sticky="nesw" -> extienda todo lo que pueda
        self.Button2 = tk.Button(self.TopFrame, text="Parameters", bg='blue', fg="white", command=self.parametersClicked)
        self.Button2.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")
        self.Button3 = tk.Button(self.TopFrame, text="Get Value", bg='yellow', fg="black", command=self.getValueClicked)
        self.Button3.grid(row=0, column=2, padx=5, pady=5, sticky="nesw")
        self.value = tk.StringVar()
        self.valueLabel = tk.Label(self.TopFrame, borderwidth=2, relief="groove", textvariable=self.value)
        self.valueLabel.grid(row=0, column=3, padx=5, pady=5, sticky="nesw")
        self.Button5 = tk.Button(self.TopFrame, text="Button 5", bg='pink', fg="black", command=self.button1Clicked)
        self.Button5.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nesw")  # columnspan =4 -> expande 4 columnas

        self.inputFrame = tk.Frame(self.TopFrame)
        tk.Label(self.inputFrame, text='Name').grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
        self.entryName = tk.Entry(self.inputFrame)
        self.entryName.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")
        tk.Label(self.inputFrame, text='Age').grid(row=0, column=2, padx=5, pady=5, sticky="nesw")
        self.entryAge = tk.Entry(self.inputFrame)
        self.entryAge.grid(row=0, column=3, padx=5, pady=5, sticky="nesw")
        self.Button6 = tk.Button(self.inputFrame, text="Enter new user", bg='green', fg="white", command=self.enterUserClicked)
        self.Button6.grid(row=0, column=4, padx=5, pady=5, sticky="nesw")
        self.inputFrame.grid(row=2, column=0, columnspan=4, padx=250, pady=5, sticky="nesw")

        return self.TopFrame

    def button1Clicked(self):
        messagebox.showinfo('information', 'Hello')

    def getValueClicked(self):
        self.client.publish('getValue')
        self.client.subscribe('Value')

    def enterUserClicked(self):
        self.rightFrameClass.PutEntry(self.entryName.get(), self.entryAge.get())
        print('Name ', self.entryName.get(), 'Age ', self.entryAge.get())

    def setRightFrame(self,rightFrameClass):
        self.rightFrameClass = rightFrameClass

    def parametersClicked(self):
        newWindow = tk.Toplevel(self.TopFrame) # Creamos  new Window asociada a la pantalla donde estamos = TopFrame
        newWindow.title("Parameter Window")

        # sets the geometry of toplevel
        newWindow.geometry("800x600")
        parameterFrameClass = ParameterFrameClass()
        parameterFrame = parameterFrameClass.buildFrame(newWindow, self.client)
        parameterFrame.pack(fill="both", expand="yes", padx=10, pady=10)

    def putValue(self, value):
        self.value.set(value)






