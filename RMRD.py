import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
def RMRD(data_bytes):
    """
    RAW ADC Data(RADC) is a data
    This in an byte array of legth 786432, containing raw data from the 3 ADC in the radar, one for each antenna.
    Its encoded using UINT16

    descriotion
    RX1: 0-262144
        Chirp 0: I-channel sample 0-255, Q-channel sample 0-255
        ... to
        Chirp 255: I-channel sample 0-255, Q-channel sample 0-255

    RX2: 262144-524288
        Chirp 0: I-channel sample 0-255, Q-channel sample 0-255
        ... to
        Chirp 255: I-channel sample 0-255, Q-channel sample 0-255

    RX3: 524288-786432
        Chirp 0: I-channel sample 0-255, Q-channel sample 0-255
        ... to
        Chirp 255: I-channel sample 0-255, Q-channel sample 0-255



    Args:
        data_bytes (_type_): _description_
    """

    
    print("Data length: ", len(data_bytes))
    data = np.frombuffer(data_bytes,dtype=np.uint32)
    
    
    print("Data length: ", len(data))
    
    data = data.reshape(256,256)
    np.savetxt("data.txt", data, delimiter=",")
    
    
    plt.imshow(data, cmap='plasma', interpolation='nearest')
    plt.show()
    
    plt.savefig(f"figures/RMRD_plot{datetime.now()}.svg")

    
