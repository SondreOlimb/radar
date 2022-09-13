import socket, time
HOST = "192.168.16.2"  # The server's hostname or IP address
PORT = 6172  # The port used by the server

def decode_PDAT(data):
    for i in range(0,len(data),12):
        object_range = int.from_bytes(data[0+i:2+i],byteorder="little",signed=False)
        speed = int.from_bytes(data[2+i:4+i],byteorder="little",signed=False)
        azimuth = int.from_bytes(data[4+i:6+i],byteorder="little",signed=True)
        elivation = int.from_bytes(data[6+i:8+i],byteorder="little",signed=True)
        magnitude = int.from_bytes(data[8+i:10+i],byteorder="little",signed=False)
        print("#########PDAT############ ")
        print("Range",object_range)
        print("Speed",speed)
        print("Azimuth",azimuth)
        print("Elivation",elivation)
        print("Magnitude",magnitude,"\n")
    return 0

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
    count = 786432
    while True:
    
        data = client_socket.recv(2**20) #786432+16
        try:
            data_len = len(data)
            print(len(data))
            if(len(data) <= 8):
                data_type = data[:4].decode()
                print("TYPE: ",data_type)
            
            
                length = int.from_bytes(data[4:8],byteorder="little",signed=False)
                print("length:",length)
            else:
                print(list(data))
                print(int.from_bytes(data[0:1],byteorder="little",signed=False))
                
                #print(data)
            
                
            
            if(length >0 and data_type=="PDAT"):
                decode_PDAT(data[8:])
                # print("NON-ZERP")
                # print(int.from_bytes(data[8:8+2],byteorder="little",signed="false"),"\n")
                
            # else:
            #     print("ZER0")
            #     print(data[8:12].decode(),"\n")
            
            
        
            
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
