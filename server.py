#!/usr/bin/env python3
from threading import Thread
import socket
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224   
def ricevi_comandi(sock_service, addr_client):
    while True:
        
        print("\nConnessione ricevuta da " + str(addr_client))
        print("\nAspetto di ricevere i dati ")
        contConn=0
        while True:
            dati = sock_service.recv(2048)
            contConn+=1
            if not dati:
                print("Fine dati dal client. Reset")
                break
            dati = dati.decode()
            operazione, primo, secondo = dati.split(';')
            print("Ricevuto: '%s'" % dati)
            if dati=='ko':
                print("Chiudo la connessione con " + str(addr_client))
                break
            operazione, primo, secondo = dati.split(';')
            if operazione == "più" :
                risultato = int(primo) + int(secondo)
            if operazione == "meno" :
                risultato = int(primo) - int(secondo)
            if operazione == "per" :
                risultato = int(primo) * int(secondo)
            if operazione == "diviso" :
                risultato = int(primo) / int(secondo)
            dati = "il risultato dell'operazione: " + operazione + " tra "+ primo+ " e "+ secondo+ " è: "+ str(risultato)
            dati = dati.encode()
            sock_service.send(dati)
        sock_service.close()        

def avvia_server(indirizzo, porta ):
    sock_listen = socket.socket()
    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_listen.bind((indirizzo, porta))
    sock_listen.listen(5)
    print("Server in ascolto su %s." % str((indirizzo, porta)))
    ricevi_connessioni(sock_listen)
    
def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da %s " % str(addr_client))
        print("Creo un thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("il thread non si avvia")
            sock_listen.close()
if __name__ == '__main__':
    avvia_server(SERVER_ADDRESS,SERVER_PORT)