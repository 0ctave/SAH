import socket


#def data_process(data)




HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


def process_data(data):
    str = data.decode("utf-8", "strict")



    if str == "STOP":
        return True
    return False


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    stopped = False
    while not stopped:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                stopped = process_data(data)
                conn.sendall(data)
