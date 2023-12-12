import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.ticker
import os
import tables as tt
# for navigation
import pandas as pd

# for file creation
import h5py
# open .tifs
from PIL import Image
from tifffile import imread



# where's the data?
datafolder = './Aikin_Data'
# metadata dictionary
meta = {}

# what are the folder names in the data folder? (alphabetical)
ts_fnames = sorted([entry for entry in os.listdir(datafolder) 
                if os.path.isdir(os.path.join(datafolder, entry)) and 'DS_Store' not in entry])
meta['ts_filenames'] = ts_fnames

# how many thin sections are there?
ts_count = len(ts_fnames)

meta['ts_count'] = ts_count

# let's also establish some more compact naming
ts_names = ['H1', 'H2', 'C1', 'C2']
meta['ts_names'] = ts_names


for i, ts in enumerate(ts_fnames):

    # what are the names names of the individual map files?
    map_fnames = sorted([entry for entry in os.listdir(os.path.join(datafolder, ts, 'RAW'))
                if 'DS_Store' not in entry])
    meta[f'{ts_names[i]}_map_filenames'] = map_fnames


    # number of maps for this thin section
    map_count = len(map_fnames)
    meta[f'{ts_names[i]}_map_count'] = map_count
    print(meta[f'{ts_names[i]}_map_filenames'])
    
    
    # locate the element name in the filename    
    # the element names always follow 'full_'
    start = lambda x: x.find('full_') + 5
    end = lambda y: y.find('full_') + 7

    # list the snipped element names. 
    element_names = [i[start(i):end(i)].replace(" ", "") for i in meta[f'{ts_names[i]}_map_filenames']]
    #print(element_names)