import tkinter as tk

import numpy as np
import cv2 as cv

from PIL import Image as Img
from PIL import ImageTk


class LeftFrameClass:

    def buildFrame(self,fatherFrame, client):
        self.client = client
        self.LeftFrame = tk.LabelFrame(fatherFrame, text='Left')

        self.Button1 = tk.Button(self.LeftFrame, text="Start video stream", bg='green', fg="white",
                                 command=self.startVideoClicked)
        self.Button1.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
        self.Button2 = tk.Button(self.LeftFrame, text="Stop video stream", bg='red', fg="white",
                                 command=self.stopVideoClicked)
        self.Button2.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")

        self.canvas = tk.Canvas(self.LeftFrame)
        self.canvas.grid(row=1, column=0, columnspan=2, sticky="nesw")

        return self.LeftFrame

    def startVideoClicked(self):
        self.client.publish('StartVideoStream')
        self.client.subscribe('videoFrame')

    def stopVideoClicked(self):
        self.client.publish('StopVideoStream')

    def SetFrame(self, jpg_original):
        jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
        img = cv.imdecode(jpg_as_np, 1)
        self.photo = ImageTk.PhotoImage(image=Img.fromarray(img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)