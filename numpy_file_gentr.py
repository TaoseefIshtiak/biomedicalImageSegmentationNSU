from glob import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

temp = []

for i in glob('data/y_train/*.png'):
    img = Image.open(i)
    img_arr = np.array(img)
    temp.append(img_arr)

temp = np.array(temp)
np.save('y_train', temp) 