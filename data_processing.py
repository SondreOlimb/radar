import RADC
import RMRD
def data_processing(data_bytes):
    try:
      
        data_type = data_bytes[:4].decode()
        print("TYPE: ", data_type)
        length = int.from_bytes(
            data_bytes[4:8], byteorder="little", signed=False)
        print("length:", length)
        print(data_bytes[8+length:8+length+4])
        
        if(data_type == "ADC"):
            RADC.RADC(data_bytes=data_bytes[8:8+length])
        data_type = data_bytes[8+length:8+length+4].decode()
        length_2 = int.from_bytes(
            data_bytes[8+length+4:8+length+4+4], byteorder="little", signed=False)
        print(length_2)
        if(data_type == "RMRD"):
            RMRD.RMRD(data_bytes=data_bytes[8+length+8:8+length+8+length_2])
    except KeyboardInterrupt:
        print("Keyboard abort")
        
        