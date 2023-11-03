# --*--coding:utf-8--*--
# Time : 2023/3/30 16:38
# Author : airy
# File : ground-truth-show.py
import cv2
import os

import matplotlib


class Colors:
    # Ultralytics color palette https://ultralytics.com/
    def __init__(self):
        # hex = matplotlib.colors.TABLEAU_COLORS.values()
        hex = ('FF95C8','FF3838',  '8438FF', '344593',  '00C2FF','FFB21D', 'CFD231','0018EC' ,  '48F90A', '92CC17', '3DDB86', '1A9334', '00D4BB',
               '2C99A8', 'FF701F','6473FF','520085', 'CB38FF',  'FF9D97', 'FF37C7')
        # hex = ('FF3838', 'FF9D97', 'FF701F', 'FFB21D', 'CFD231', '48F90A', '92CC17', '3DDB86')
        self.palette = [self.hex2rgb('#' + c) for c in hex]
        self.n = len(self.palette)

    def __call__(self, i, bgr=False):
        c = self.palette[int(i) % self.n]
        return (c[2], c[1], c[0]) if bgr else c

    @staticmethod
    def hex2rgb(h):  # rgb order (PIL)
        return tuple(int(h[1 + i:1 + i + 2], 16) for i in (0,2,4))

colors = Colors()
names= ['bus', 'bicycle', 'car', 'motorcycle', 'person', 'rider', 'train', 'truck']
def draw_box_in_single_image(image_path, txt_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 读取txt文件信息
    def read_list(txt_path):
        pos = []
        with open(txt_path, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()  # 整行读取数据
                if not lines:
                    break
                # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
                p_tmp = [float(i) for i in lines.split(' ')]
                pos.append(p_tmp)  # 添加新读取的数据
                # Efield.append(E_tmp)
                pass
        return pos


    # txt转换为box
    def convert(size, box):
        xmin = (box[1]-box[3]/2.)*size[1]
        xmax = (box[1]+box[3]/2.)*size[1]
        ymin = (box[2]-box[4]/2.)*size[0]
        ymax = (box[2]+box[4]/2.)*size[0]
        box = (int(xmin), int(ymin), int(xmax), int(ymax))
        return box

    pos = read_list(txt_path)
    print(pos)
    tl = int((image.shape[0]+image.shape[1])/2)
    lf = max(tl-1,1)
    for i in range(len(pos)):
        # label = str(int(pos[i][0]))
        label = names[int(pos[i][0])]
        print('label is '+label)
        box = convert(image.shape, pos[i])
        image = cv2.rectangle(image,(box[0], box[1]),(box[2],box[3]),colors(int(pos[i][0])),thickness=2)
        # cv2.putText(image,label,(box[0],box[1]-2), 0, 1,colors(int(pos[i][0])),thickness=1, lineType=cv2.LINE_AA)

        pass

    if pos:
        cv2.imwrite('D:/see/{}.png'.format(image_path.split('\\')[-1][:-4]), image)
    else:
        print('None')


    print('D:/see/{}.png'.format(image_path.split('\\')[-1][:-4]))
    # cv2.imshow("images", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


img_folder = "D:/tri-val"
img_list = os.listdir(img_folder)
img_list.sort()

label_folder = "D:/tri-val-label"
label_list = os.listdir(label_folder)
label_list.sort()

for i in range(len(img_list)):
    image_path = img_folder + "\\" + img_list[i]
    txt_path = label_folder + "\\" + label_list[i]
    draw_box_in_single_image(image_path, txt_path)

