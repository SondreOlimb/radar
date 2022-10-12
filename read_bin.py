import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import data_processing
try:
    with open("felttest2/Record_2022-09-28_14-48-46/Record_2022-09-28_14-48-46.bin", "rb") as f:
        data = f.read()
    data_processing.data_processing(data)
        
        
except IOError as e:
    print(e)
