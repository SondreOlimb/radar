import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
def RADC(data_bytes):
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
    data = np.frombuffer(data_bytes,dtype=np.uint16)
    print("Data length: ", len(data))
    fig, axs = plt.subplots(3, 1)
    axs[0].plot(data[:256])
    axs[0].plot(data[256:256+256])
    axs[1].plot(data[256*3:256*3+256])
    axs[1].plot(data[256*4:256*4+256])
    axs[2].plot(data[256*6:256*6+256])
    axs[2].plot(data[256*7:256*7+256])
    plt.show()
    plt.savefig(f"figures/plot{datetime.now()}.svg")

    
