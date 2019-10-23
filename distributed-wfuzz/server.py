import wfuzz
import socket
import pickle
import select

HOST = '127.0.0.1'
PORT = 65432

MSG_DONTWAIT = 0x40

def fuzz_command(command, words, conn):
    s = wfuzz.get_session(command)

    # Clear out the wordlist file specifier
    s.data["payloads"] = None

    s.get_payloads([words])

    for r in s.fuzz():
        conn.sendall((r.__str__() + "\n").encode("utf-8"))
    
    conn.sendall("$$\n".encode("utf-8"))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        conn.setblocking(0)
        with conn:
            print('Connected by', addr)

            command = ""
            words_data = b''

            reading_words = False
            print("Reading input")
            while True:
                ready = select.select([conn], [], [], 1)
                if ready[0]:
                    data = conn.recv(1)

                    if not data:
                        break

                    if (data == b'\n' and reading_words == False):
                        reading_words = True
                        continue
                    
                    if reading_words:
                        words_data += data
                    else:
                        command += data.decode("utf-8")
                else:
                    break
            
            words = pickle.loads(words_data)

            print("Running fuzz")
            fuzz_command(command, words, conn)
            print("Fuzz finished")