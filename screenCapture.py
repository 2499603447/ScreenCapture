from PIL import ImageGrab
import numpy as np
import cv2
import ctypes
try:
    temp = ctypes.windll.LoadLibrary('opencv_ffmpeg345_64.dll')
except:
    pass
screen = ImageGrab.grab()  # 获得当前屏幕

length, width = screen.size  # 获得当前屏幕的大小
video_decode_style = cv2.VideoWriter_fourcc(*'XVID')  # 编码格式
video = cv2.VideoWriter('a.avi', video_decode_style, 32, (length, width))  # 输出文件命名为a.mp4,帧率为32，可以调节
print("starting capture!")
while True:
    im = ImageGrab.grab()
    imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)  # 转为opencv的BGR格式
    video.write(imm)

    # if ord(msvcrt.getch()) == 27:
    #     break
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

video.release()
print("video has been released!")
cv2.destroyAllWindows()