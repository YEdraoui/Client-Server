import socket

# Define the server address and port
server_host = ''  # Accept connections from any address
server_port = 12345       # Choose any port that is not reserved

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind((server_host, server_port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server listening on {server_host}:{server_port}")

# Wait for a client to connect
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} has been established!")

# Receive data from the client
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"Received from client: {data}")
    
    # Send data back to the client
    client_socket.send("Data received".encode())

# Close the connection
client_socket.close()
server_socket.close()
