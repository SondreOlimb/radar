if(length >0 and data_type=="PDAT"):
                decode_PDAT(data[8:])
                # print("NON-ZERP")
                # print(int.from_bytes(data[8:8+2],byteorder="little",signed="false"),"\n")
                
            # else:
            #     print("ZER0")
            #     print(data[8:12].decode(),"\n")

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