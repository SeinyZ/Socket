
import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
def connessione_server(address, port):
    sock_service = socket.socket()
    sock_service.connect((address, port))
    print("Connesso a " + str((address, port)))
    invia_comandi(sock_service)
    sock_service.close()
def invia_comandi(sock_service):
    while True:
        try:
            dati = input("Inserisci i dati da inviare (digita ko per uscire): ")
        except EOFError:
            print("\nOkay. Exit")
            break
        if not dati:
            print("Non puoi inviare una stringa vuota!")
            continue
        if dati == 'ko':
            print("Chiudo la connessione con il server!")
            break
        #trasforma la string in byte
        dati = dati.encode()

        sock_service.send(dati)

        dati = sock_service.recv(2048)

        if not dati:
            print("Server non risponde. Exit")
            break
        
        dati = dati.decode()

        print("Ricevuto dal server:")
        print(dati + '\n')

if __name__ == '__main__':
    connessione_server(SERVER_ADDRESS, SERVER_PORT)