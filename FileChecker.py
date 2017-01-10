import os, time
import shutil
while True:
    time.sleep(1)
    targetDirectory = os.listdir('\\Users\\Norioki\\Downloads')
    for i in targetDirectory:
        if i.endswith(".osz"):
            shutil.move('\\Users\\Norioki\\Downloads\\'+ i,'\\Users\\Norioki\\Desktop\\Laugh Out Loud\\abshd\\a\\cofeee\\New folder\\poo\osu!\\Songs\\' + i)
