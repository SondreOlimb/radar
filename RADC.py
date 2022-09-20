import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
def RADC(data_bytes):

    
    if(len(data_bytes) <= 8):
                data_type = data_bytes[:4].decode()
                print("TYPE: ",data_type)
            
            
                length = int.from_bytes(data_bytes[4:8],byteorder="little",signed=False)
                print("length:",length)
    else:
        data = np.frombuffer(data_bytes,dtype=np.uint16)
        plt.figure()
        plt.plot(data[:512])
        plt.savefig(f"figures/plot{datetime.now()}.svg")

    
