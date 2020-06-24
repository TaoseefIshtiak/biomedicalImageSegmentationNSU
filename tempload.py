from segmentation_models import Unet, Nestnet, Xnet
from keras.models import Model
from keras.models import load_model
new_model = load_model("C:/Users/nsuic/Ashfia Miss Research/Ashfia Miss Research/UNetPlusPlus-master/UNetPlusPlus-master/trained_weights/brats2013/run_1/Nestnet-vgg16-random.h5")
new_model.summary()
