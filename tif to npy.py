import numpy as np
import PIL
from PIL import Image
img = Image.open('vis_dest/case_00000/00308.png')
img_arr = np.array(img)
print(img_arr)
np.save('geekfile', img_arr) 

