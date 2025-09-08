from tkinter import *
import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
topic = "IoT-IF-Undip"

def send_on():
    client.publish(topic, params[0])

client = mqtt.Client()
client.connect(broker, 1883, 60)

#---GUI---#
root = Tk()
root.title("Kontrol LED IoT")

Label(root, text="Input teks").grid(row=0)

teks = Entry(root)

teks.grid(row=0,column=1)

def getInput():
    ini = teks.get()
    
    global params
    params = [ini]

Button(root, text = "submit", command = getInput).grid(row = 5, sticky = W)
Button(root, text = "kirim", command=send_on).grid(row = 6,sticky = W)

root.mainloop()


