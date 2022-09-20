import matplotlib.pyplot as plt
import numpy as np

try:
    with open("Record_2022-09-20_16-25-11.bin", "rb") as f:
        data = f.read()

        data_type = data[:4].decode()
        print("TYPE: ", data_type)
        length = int.from_bytes(
            data[4:8], byteorder="little", signed=False)
        print("length:", length)
        data = data[8:]
        data = np.frombuffer(data,dtype=np.uint16)
        plt.figure()
        plt.plot(data[:512])
        plt.show()
        plt.savefig(f"figures/plot.svg")


except IOError as e:
    print(e)
