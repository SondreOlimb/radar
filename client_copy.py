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
            RADC.RADC(data=data)
            
        
            
        except Exception as e:
            print("Error:",e)
            client_socket.close()
            break
        print("\n")
        time.sleep(2)
    
    
    # length = int.from_bytes(data[4:8],byteorder="little")
    # print("data length",len(data))
  
    # print("TYPE: ",int.from_bytes(data[4:8],byteorder="little"))
    # raw_payload =data[8:8+length]
    # print(8)
    # print("TYPE: ",int.from_bytes(data[13:13+4],byteorder="little"))
    # #print("TYPE: ",data[8:12].decode())

        

    # except:
    #     print("TYPE: NO type" )
    # cl
    

    #print("RECEIVED: %s" % data, "\n")

    #b = bytearray(data,encoding="utf-8")
    #print(data.decode("utf-8"))
    

    #data = input("SEND( TYPE q or Q to Quit):")
    #client_socket.send(data)
    #if data.lower() == 'q':
    #
except KeyboardInterrupt:
    print("Keyboard abort")
    client_socket.close()
    
    #    break
