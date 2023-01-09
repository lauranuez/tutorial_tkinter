import tkinter as tk

import numpy as np
import cv2 as cv

from PIL import Image as Img
from PIL import ImageTk


class LeftFrameClass:

    def buildFrame(self,fatherFrame, client):
        self.client = client
        self.mode = 'normal'
        self.LeftFrame = tk.LabelFrame(fatherFrame, text='Left')

        self.LeftFrame.rowconfigure(0, weight=1)
        self.LeftFrame.rowconfigure(1, weight=1)

        self.LeftFrame.columnconfigure(0, weight=1)
        self.LeftFrame.columnconfigure(1, weight=1)
        self.LeftFrame.columnconfigure(2, weight=1)
        self.LeftFrame.columnconfigure(3, weight=1)

        self.Button1 = tk.Button(self.LeftFrame, text="Start video stream", bg='green', fg="white",
                                 command=self.startVideoClicked)
        self.Button1.grid(row=0, column=0, columnspan = 2, padx=5, pady=5, sticky="nesw")
        self.Button2 = tk.Button(self.LeftFrame, text="Stop video stream", bg='red', fg="white",
                                 command=self.stopVideoClicked)
        self.Button2.grid(row=0, column=2, columnspan = 2, padx=5, pady=5, sticky="nesw")

        self.canvas = tk.Canvas(self.LeftFrame)
        self.canvas.grid(row=1, column=0, columnspan=3, sticky="nesw")

        self.buttonsFrame = tk.LabelFrame(self.LeftFrame, text="Image processing")
        self.buttonsFrame.grid(row=1, column=3, sticky="nesw")
        self.NormalButton = tk.Button(self.buttonsFrame, width=10, text="Normal", bg='green', fg="white",
                                      command=self.normal).pack(pady=10)
        self.GrayButton = tk.Button(self.buttonsFrame, width=10, text="Gray", bg='blue', fg="white",
                                    command=self.gray).pack(pady=10)
        self.CannylButton = tk.Button(self.buttonsFrame, width=10, text="Canny", bg='yellow', fg="black",
                                      command=self.canny).pack(pady=10)

        return self.LeftFrame

    def startVideoClicked(self):
        self.client.publish('StartVideoStream')
        self.client.subscribe('videoFrame')

    def stopVideoClicked(self):
        self.client.publish('StopVideoStream')

    def SetFrame(self, jpg_original):
        jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
        img = cv.imdecode(jpg_as_np, 1)
        if self.mode == 'normal':
            res = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        if self.mode == 'gray':
            res = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        if self.mode == 'canny':
            res = cv.Canny(img, 50, 100)
        self.photo = ImageTk.PhotoImage(image=Img.fromarray(res))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

    def normal(self):
        self.mode = 'normal'

    def gray(self):
        self.mode = 'gray'

    def canny(self):
        self.mode = 'canny'