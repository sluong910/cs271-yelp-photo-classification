import cv2
import matplotlib.pyplot as plt
import os
import glob

def viewImg(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgplot = plt.imshow(img)
    plt.show()

def compressImg(img):
    H, W, _ = img.shape
    img = cv2.resize(img, (W//2,H//2), interpolation=cv2.INTER_CUBIC)

    return img

if __name__ == "__main__":
    input_folder = r'./train_50/photos'
    output_folder = r'./train_50/photos_compressed'
    input_list = glob.glob(os.path.join(input_folder, '*.jpg'))
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for inPath in input_list:
        outPath = inPath.replace(input_folder, output_folder).replace('.jpg','_LR.jpg')

        img_H = cv2.imread(inPath)
        img_L = compressImg(img_H)

        cv2.imwrite(outPath, img_L)
