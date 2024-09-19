import socket

# Define the server address and port
server_host = 'localhost'  # If running on the same machine
server_port = 12345        # Same port as the server

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))
print(f"Connected to server at {server_host}:{server_port}")

# Send data to the server
while True:
    message = input("Enter message to send to server (type 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    
    # Send the message to the server
    client_socket.send(message.encode())
    
    # Receive the server's response
    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")

# Close the connection
client_socket.close()
