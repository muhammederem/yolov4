import os
import glob
MAIN_DIR = 'C:\\Users\\faruk\\Documents\\ASTRID\\Yolov4\\'
DATASET_DIR = os.path.join(MAIN_DIR, "images_labels")
IMAGES_DIR = os.path.join(DATASET_DIR, "*.jpg")

for img in glob.glob(DATASET_DIR+"/*.png"):
    os.rename(img, img[:-3]+"jpeg")
    print(img)

