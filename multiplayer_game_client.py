import socket

# Server settings
HOST = '127.0.0.1'  # Replace with the server's IP address
PORT = 12345        # The port the server is listening on

# Function to start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Receive welcome message
    welcome_message = client_socket.recv(1024).decode()
    print(welcome_message)

    while True:
        # Receive prompt for the guess
        prompt = client_socket.recv(1024).decode()
        print(prompt, end='')

        # Get the guess from the user
        guess = input()

        # Send the guess to the server
        client_socket.send(guess.encode())

        # Receive the result of the guess
        result = client_socket.recv(1024).decode()
        print(result)

        # If the game is over, break the loop
        if "Congratulations" in result:
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()
