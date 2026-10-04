import socket

host = "127.0.0.1"
ports = [22, 80, 443, 8000, 8080]

for port in ports:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.settimeout(0.5)
        result = connection.connect_ex((host, port))

        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: connection not established")