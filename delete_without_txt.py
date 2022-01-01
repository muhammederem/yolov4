import os
import glob
MAIN_DIR = 'C:\\Users\\faruk\\Documents\\ASTRID\\Yolov4\\'
DATASET_DIR = os.path.join(MAIN_DIR, "images_labels")
IMAGES_DIR = os.path.join(DATASET_DIR, "*.jpg")


test = []
train =[]
images = []
txt = []

count = 0


for img in glob.glob(DATASET_DIR+"/*.jpeg"):
    start_name = img.find('Yolov4')+21
    full = img[start_name:]
    images.append(full[:-5])
    full = "/content/drive/My Drive/ASTRID/darknet/ObjectDetection/images_and_labels/"+full

for img in glob.glob(DATASET_DIR+"/*.txt"):
    start_name = img.find('Yolov4')+21
    full = img[start_name:]
    txt.append(full[:-4])
    
    
for image in txt:
    if image in images:
        if count % 5 == 0:
            test.append(full)
        else:
            train.append(full)
        count +=1

with open('valid.txt', 'w',encoding="utf-8") as f:
    for line in test:
        print(line)
        f.write("/content/drive/My Drive/ASTRID/darknet/ObjectDetection/images_and_labels/"+line)
        f.write('\n')

with open('train.txt', 'w',encoding="utf-8") as f:
    for line in train:
        print(line)
        f.write("/content/drive/My Drive/ASTRID/darknet/ObjectDetection/images_and_labels/"+line)
        f.write('\n')
   


