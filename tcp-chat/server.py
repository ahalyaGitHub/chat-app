import socket
import threading

def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Listen on all interfaces
    server_socket.listen(5)  # Allow up to 5 clients

    print("TCP Server started...")
    clients = []

    def broadcast_message(message, sender):
        for client in clients:
            if client != sender:  # Send to all clients except the sender
                try:
                    client.send(message.encode())
                except:
                    clients.remove(client)

    def handle_client(client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"Client: {message}")
                    broadcast_message(message, client_socket)
                else:
                    client_socket.close()
                    break
            except:
                print("Client disconnected")
                clients.remove(client_socket)
                break

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_tcp_server()