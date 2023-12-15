"""
In this script, the preprocessed signals given in the box are loaded
base and in pickle format. The pickle library needs to be installed if you don't have it
The task of this script is to extract features from possible signals so that in the next
step by step classification
"""

import numpy as np
import pickle 
import pandas as pd
import os.path
import tqdm # loading bar library, install as pip install tqdm


# Signal indices for variable data
# If you want to extract only EEG, for example, the notation is like
# data[x,EEG_ch,:] where x is the number of trials

EEG_ch = range(32);
EOG_ch = range(32,34);
EMG_ch = range(34,36);
GSR_ch = 36;
Resp_ch = 37; # respiracija
Plet_ch = 38; # pletizmograf
Temp_ch = 39; # temperatura

PATH =  os.path.dirname(__file__) + '\..\dataset\signals_processed\DEAP\s01.dat'

with open(PATH, 'rb') as f:
    data = pickle.load(f, encoding = 'bytes') 
    # If you use Python 3, you need to put encoding = 'byte' because it is
     # pickling done in Python 2
    
    
labels = pd.DataFrame(data[b'labels'], columns = ['valence','arousal', 'dominance', 'liking'])                                               

# the data is organized as a structure with dimensions 40x40x8064 (num_rial x 
data = data[b'data']


##### FEATURE EXTRACTION matrix 40 x num_of_features ########
#### Add you here with code #######

    


for i in tqdm.tqdm(range(40),desc = 'Number of trials'):
    
    signals = data[i,:,:] # signals from current trial
    eeg = signals[EEG_ch]
    emg = signals[EMG_ch]
    eog = signals[EOG_ch]
    gsr = signals[GSR_ch]
    plet = signals[Plet_ch]
    resp = signals[Resp_ch]
    temp = signals[Temp_ch]
    
    





#### 

