import socket
import threading

def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 12345))  # Listen on all interfaces

    print("UDP Server started...")
    clients = set()  # To keep track of client addresses

    def handle_client():
        while True:
            try:
                message, client_address = server_socket.recvfrom(1024)
                if client_address not in clients:
                    clients.add(client_address)  # Add new client to the set
                print(f"Received message from {client_address}: {message.decode()}")
                # Broadcast message to all clients except the sender
                for client in clients:
                    if client != client_address:
                        server_socket.sendto(message, client)
            except Exception as e:
                print(f"Error: {e}")
                break

    # Start handling client messages in a separate thread
    threading.Thread(target=handle_client, daemon=True).start()

    # Keep the server running
    while True:
        pass  # Main thread does nothing, just keeps the server alive

if __name__ == "__main__":
    start_udp_server()