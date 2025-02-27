import socket
import threading
import random

# Server settings
HOST = '0.0.0.0'  # Accept connections on all available interfaces
PORT = 12345       # The port that the server will listen on

# Global variable for the random number to guess
random_number = random.randint(1, 100)

# Function to handle each player's connection
def handle_client(client_socket, client_address):
    print(f"New connection: {client_address}")
    client_socket.send("Welcome to the Guess the Number Game!\n".encode())

    while True:
        try:
            # Ask the client for a guess
            client_socket.send("Guess a number between 1 and 100: ".encode())
            guess = client_socket.recv(1024).decode().strip()

            # Check if the guess is a valid number
            if guess.isdigit():
                guess = int(guess)
                if guess < random_number:
                    client_socket.send("Too low! Try again.\n".encode())
                elif guess > random_number:
                    client_socket.send("Too high! Try again.\n".encode())
                else:
                    client_socket.send(f"Congratulations! You guessed the number {random_number}.\n".encode())
                    break
            else:
                client_socket.send("Please enter a valid number.\n".encode())

        except Exception as e:
            print(f"Error with {client_address}: {e}")
            break

    client_socket.close()
    print(f"Connection with {client_address} closed.")

# Function to start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Server listening on {HOST}:{PORT}...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
