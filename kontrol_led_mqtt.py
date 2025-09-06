import tkinter as tk
import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
topic = "Coba"

def send_on():
    client.publish(topic, "1")
    status_label.config(text="LED ON")

def send_off():
    client.publish(topic, "0")
    status_label.config(text="LED OFF")

client = mqtt.Client()
client.connect(broker, 1883, 60)

#---GUI---#
root = tk.Tk()
root.title("Kontrol LED IoT")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

on_btn = tk.Button(frame, text="LED Nyala", command=send_on, bg="blue", fg="white")
on_btn.grid(row=0, column=0, padx=10)

off_btn = tk.Button(frame, text="LED Mati", command=send_off, bg="red", fg="white")
off_btn.grid(row=0, column=1, padx=10)

status_label = tk.Label(frame, text="Status: -")
status_label.grid(row=1,  column=0, columnspan=2, pady=10)

root.mainloop()


