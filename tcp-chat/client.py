import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Change this value for each client instance
client_number = 1  # Set this to 1 for Client 1 and 2 for Client 2

def start_tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.211.34', 12345)  # Replace with actual server IP
    client_socket.connect(server_address)

    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    # Add message to chat
                    add_message_to_chat(f"{message}", "right" if client_number == 1 else "left")
            except:
                print("Connection closed")
                break

    def send_message(event=None):
        message = message_entry.get()
        if message:
            # Add message to chat
            add_message_to_chat(f"{message}", "left" if client_number == 1 else "right")
            client_socket.send(message.encode())
            message_entry.delete(0, tk.END)

    def add_message_to_chat(message, alignment):
        chat_area.config(state=tk.NORMAL)
        if alignment == "right":
            chat_area.insert(tk.END, f"{message}\n", "right")
            chat_area.tag_configure("right_bg", background="#DCF8C6")  # Light green for user messages
            chat_area.tag_add("right_bg", f"{float(chat_area.index(tk.END)) - 2.0}", tk.END)
        else:
            chat_area.insert(tk.END, f"{message}\n", "left")
            chat_area.tag_configure("left_bg", background="#F0F0F0")  # Light gray for server messages
            chat_area.tag_add("left_bg", f"{float(chat_area.index(tk.END)) - 2.0}", tk.END)

        chat_area.config(state=tk.DISABLED)
        chat_area.yview(tk.END)

    # Tkinter GUI setup
    window = tk.Tk()
    window.title("Chat Client")
    window.geometry("400x600")
    window.minsize(400, 600)

    main_frame = tk.Frame(window, bg="#f7f7f7")
    main_frame.pack(fill=tk.BOTH, expand=True)

    chat_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 12), bg="white", padx=10, pady=10)
    chat_area.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    chat_area.tag_configure("right", justify="right", foreground="black")
    chat_area.tag_configure("left", justify="left", foreground="black")

    message_entry = tk.Entry(main_frame, font=("Arial", 14), bg="#e0e0e0", bd=0)
    message_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    message_entry.bind("<Return>", send_message)  # Bind Enter key to send_message

    send_button = tk.Button(main_frame, text="Send", command=send_message, font=("Arial", 14), bg="#25D366", fg="white", bd=0)
    send_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=0)
    main_frame.grid_rowconfigure(0, weight=1)

    threading.Thread(target=receive_messages, daemon=True).start()
    window.mainloop()

if __name__ == "__main__":
    start_tcp_client()
