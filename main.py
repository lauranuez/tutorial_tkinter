import base64
import tkinter as tk
from TopFrameClass import TopFrameClass
from RightFrameClass import RightFrameClass
from LeftFrameClass import LeftFrameClass
import paho.mqtt.client as mqtt

def on_message(cli, userdata, message):
    if message.topic == 'Value':
        topFrameClass.putValue(message.payload)

    if message.topic == 'videoFrame':
        jpg_original = base64.b64decode(message.payload)
        leftFrameClass.SetFrame(jpg_original)

def ConnectButtonClicked():
    global connected
    if not connected:
        ConnectButton['text'] = 'Disconnect'
        ConnectButton['bg'] = 'green'
        connected = True
        MainFrame.pack(fill="both", expand="yes", padx=10, pady=10)
        client.publish('Connect')
    else:
        ConnectButton['text'] = 'Connect'
        ConnectButton['bg'] = 'red'
        connected = False
        MainFrame.pack_forget()

connected = False
root = tk.Tk()
root.geometry('1200x700')
root.title('Dashboard')

broker_address = "broker.hivemq.com"
broker_port = 8000

client = mqtt.Client(transport="websockets")
client.on_message = on_message
client.connect(broker_address, broker_port)
client.loop_start()

ConnectButton = tk.Button(root, width= 150, text="Connect", bg='red', fg="white", command=ConnectButtonClicked)
ConnectButton.pack()

MainFrame = tk.Frame(root)
topFrameClass = TopFrameClass()
TopFrame = topFrameClass.buildFrame(MainFrame, client)
TopFrame.pack(fill="both", expand="yes", padx=10, pady=5)

MidFrame = tk.Frame(MainFrame)
MidFrame.pack(fill="both", expand="yes", padx=10, pady=0)

leftFrameClass = LeftFrameClass()
LeftFrame = leftFrameClass.buildFrame(MidFrame, client)
LeftFrame.pack(side=tk.LEFT, fill="both", expand="yes", padx=5, pady=5)

rightFrameClass = RightFrameClass()
RightFrame = rightFrameClass.buildFrame(MidFrame)
RightFrame.pack(side=tk.RIGHT, fill="both", expand="yes", padx=5, pady=5)
topFrameClass.setRightFrame(rightFrameClass)

BottomFrame = tk.LabelFrame(MainFrame, text='Bottom')
BottomFrame.pack(fill="both", expand="yes", padx=10, pady=5)

root.mainloop()


