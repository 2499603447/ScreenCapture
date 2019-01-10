import os
import cv2
import glob

def Opencv(pics_path):
    fps = 9
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    vedio_path=os.path.join(pics_path,"flower.avi")#视频名字
    videoWriter = cv2.VideoWriter(vedio_path, fourcc, fps, (1440, 900))#视频设置

    imgs_dir=pics_path
    file_img = glob.glob(os.path.join(pics_path, '*.jpg'))#查看目录下所有后缀为.jpg的文件

    for i in file_img:
        imgname = os.path.join(imgs_dir, i)
        #print (imgname)
        frame = cv2.imread(imgname)
        videoWriter.write(frame)#write
    videoWriter.release()#save
    for i in file_img:#移除目录下的图片
        os.remove(i)


if __name__ == '__main__':
    Opencv()
import time
import os
from datetime import datetime

from lib.winscreen import pillow_path,conf_path

from lib.screen.opencv import Opencv
from PIL import ImageGrab

def Pillow():
    print ("[root]:start print screen!")
    #time_date=datetime.now()
    #time_n=time_date.strftime("%Y%m%d-%H:%M")
    time_n=time.time()
    dir_pillow=os.path.join(pillow_path,str(time_n))
    if not os.path.exists(dir_pillow):
        os.mkdir(dir_pillow)
    while True:
        now_time = time.time()
        pic_path = os.path.join(dir_pillow, str(now_time) + ".jpg")
        im = ImageGrab.grab()#截屏
        im.save(pic_path)#保存
        with open(conf_path,"r") as fd_conf:
            data=fd_conf.read()
        result=eval(data)#str转dict
        if  result["globalvar"] == "stop":
            break

    print ("[root]:eixt print screen!")
    Opencv(dir_pillow)
    return