import numpy as np
import PIL
from PIL import Image
img = Image.open('vis_dest/case_00000/kidney.tif')
img_arr = np.array(img)
np.save('geekfile', img_arr) 

