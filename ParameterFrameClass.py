import json
import tkinter as tk


class ParameterFrameClass:

    def buildFrame(self, fatherFrame, client):
        self.client = client
        self.fatherFrame = fatherFrame
        self.ParameterFrame = tk.Frame(fatherFrame)
        self.ParameterFrame.rowconfigure(0, weight=4)
        self.ParameterFrame.rowconfigure(1, weight=1)
        self.ParameterFrame.rowconfigure(2, weight=1)

        self.ParameterFrame.columnconfigure(0, weight=1)
        self.ParameterFrame.columnconfigure(1, weight=1)

        self.radioButtonFrame = tk.LabelFrame(self.ParameterFrame, text="Radio button group")
        self.radioButtonFrame.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")

        self.var = tk.StringVar()
        self.var.set("Madrid")
        tk.Radiobutton(self.radioButtonFrame, text="Madrid", variable=self.var, value="Madrid").pack()
        tk.Radiobutton(self.radioButtonFrame, text="Barcelona", variable=self.var, value="Barcelona").pack()
        tk.Radiobutton(self.radioButtonFrame, text="Sevilla", variable=self.var, value="Sevilla").pack()
        tk.Radiobutton(self.radioButtonFrame, text="Jaen", variable=self.var, value="Jaen").pack()

        self.checkBoxFrame = tk.LabelFrame(self.ParameterFrame, text="Check box group")
        self.checkBoxFrame.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")
        self.checkOptions = ['uno', 'dos', 'tres', 'cuatro']
        self.selected = []
        self.checkBox = []

        for option in self.checkOptions:
            self.selected.append(tk.Variable(value=0))
            self.checkBox.append(tk.Checkbutton(self.checkBoxFrame, text=option, variable=self.selected[-1]).pack())

        self.scale = tk.Scale(self.ParameterFrame, from_=0, to=100, orient=tk.HORIZONTAL)
        self.scale.set(50)
        self.scale.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nesw")

        self.closeButton = tk.Button(self.ParameterFrame, text="Send parameters and close", bg='red', fg="white",
                                     command=self.closeButtonClicked)
        self.closeButton.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nesw")

        return self.ParameterFrame

    def closeButtonClicked(self):
        MsgBox = tk.messagebox.askquestion(parent=self.ParameterFrame, title='Send Parameters',
                                           message='Are you sure you want to send these values',
                                           icon='warning')
        if MsgBox == 'yes':
            selectedOptions = []
            for i in range(0, len(self.checkOptions)):
                if self.selected[i].get() == '1':
                    selectedOptions.append(self.checkOptions[i])

            parameters = {
                'radio': self.var.get(),
                'scale': self.scale.get(),
                'selectedOptions': selectedOptions
            }
            self.client.publish('writeParameters', json.dumps(parameters))
            tk.messagebox.showinfo(parent=self.ParameterFrame, title='Return',
                                   message='You will now return to the main application screen')
            self.fatherFrame.destroy()
