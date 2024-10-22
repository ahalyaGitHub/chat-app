# Chat Application

This project is a simple chat application built using Python, utilizing TCP and UDP protocols for communication between clients and a server. The application provides a user-friendly interface using Tkinter.

## Features

- Real-time messaging between clients
- Separate clients and server implementations
- User-friendly interface with message alignment
- Background colors for sent and received messages

## Project Structure

    chat-app/ 
        |-- client1/ 
            ├── client.py # Client 1 implementation 
        |-- client2/ 
            ├── client.py # Client 2 implementation 
        |-- server/ 
            ├── server.py # Server implementation

## Installation

    1. Clone the repository:
        bash
        $ git clone https://github.com/yourusername/chat-app.git
        $ cd chat-app
    
    2. Ensure you have Python installed on your system.

## Usage

Start the Server in Server System

    1. Navigate to the server directory:
                $ cd server
       
    3. Run the server script:
                $ python server.py

## Start the Clients

1. Open two terminal windows for Client 1 and Client 2.

2. Navigate to the respective client directories:

       For Client 1:
           $ cd client1
    
       For Client 2:
           $ cd client2

3. Run the client scripts:
   $ python client.py

## Configuration

Make sure to set the server IP address in the client scripts.

You may need to modify firewall settings to allow communication through the specified port.

## Termination

To terminate the server, you may need to manually stop it in the terminal (Ctrl+C may not work in all cases).
