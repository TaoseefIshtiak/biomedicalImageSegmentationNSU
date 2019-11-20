from helper_functions import *
#from BRATS2013_application import *
# x_data = np.array( [np.array(cv2.imread("0_predict.png"))] )
# print("x data"+ str(x_data))
# pixels = x_data.flatten().reshape(196, 1000)
# print (pixels.shape)
target = cv2.imread("0_predict.png")
prediction = cv2.imread("29_predict.png")
intersection = np.logical_and(target, prediction)
union = np.logical_or(target, prediction)
iou_score = np.sum(intersection) / np.sum(union)
print(iou_score)
print("authors code output below")
print(compute_iou(cv2.imread("0_predict.png"), cv2.imread("29_predict.png")))