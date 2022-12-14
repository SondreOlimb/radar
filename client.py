import socket, time
import matplotlib.pyplot as plt
import numpy as np
import RADC


HOST = "192.168.16.2"  # The server's hostname or IP address
PORT = 6172  # The port used by the server



#def decode_RADC(data):



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((HOST,PORT))
    print("Connected to:")
    print("HOST: ", HOST)
    print("PORT:",PORT,"\n")
except:
    print("Failed to connect to:")
    print("HOST: ", HOST)
    print("PORT:",PORT,"\n")
    exit()

try:
    
    while True:
    
        data = client_socket.recv(2**20) #786432+16
        try:
            RADC.RADC(data_bytes=data)
            
        
            
        except Exception as e:
            print("Error:",e)
            client_socket.close()
            break
        print("\n")
        time.sleep(2)
    
    
    
    

    
except KeyboardInterrupt:
    print("Keyboard abort")
    client_socket.close()
    
    #    break
