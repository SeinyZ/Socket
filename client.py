
import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

sock_service = socket.socket()

sock_service.connect((SERVER_ADDRESS, SERVER_PORT))

print("Client connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))

modello=["SYN", "SYN ACK", "ACK with Data", "ACK for Data"]
step=0
dati = str(step)

while True:
    dati=dati.encode() 
    sock_service.send(dati)
    print("Inviato:" + str(step) + " - " + modello[step])
    

    dati = sock_service.recv(2048)

    if not dati:
        print("Server non risponde. Exit")
        break

    dati = dati.decode()
    step = int(dati)

    if dati == '3':
        print("Ricevuto:" + str(step) + " - " + modello[step])
        print("Termino la connessione con il server.")
        break

    else:
        step = int(dati)
        print("Ricevuto:" + str(step) + " - " + modello[step])
        step+=1
        dati= str(step)

sock_service.close()