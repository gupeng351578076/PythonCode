__author__ = 'mocy'
#coding:UTF-8
import urllib.request
import pytesseract
import sys
import os
from PIL import Image,ImageEnhance,ImageDraw,ImageFilter
class ReImg:
    def getValidate(self,i):
        img_url = 'http://passport.cqzuxia.com/account/LoadValidCode'
        img_data = urllib.request.urlopen(img_url).read()
        #改变当前工作目录
        workbefore = os.getcwd()+"\\ValidateImage"
        os.chdir(workbefore)
        #写图片
        temp_file = open("validate"+str(i)+".png", 'wb')
        temp_file.write(img_data)
        temp_file.close()
        #改变工作目录回去
        workafter = os.getcwd()[:-14]
        os.chdir(workafter)

    def recongniseImg(self,file,i):
        cwd = os.getcwd()
        im=Image.open(cwd+"\\"+file+"\\validate"+str(i)+".png")
        #图片降噪
        #干扰线去除
        #保存修过的图片
        im.save(cwd+"\\ValidateImage\\image_code"+str(i)+".png")
        joinf = cwd+"\\"+file+"\\image_code"+str(i)+".png"
        image1 = Image.open(joinf)
        image1.load()
        code = pytesseract.image_to_string(image1)
        print(code)
        print("----------")


rei = ReImg()
import sys
import io
#改变python3默认输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
for x in range(5):
    rei.getValidate(x)
for y in range(5):
    rei.recongniseImg("ValidateImage",y)
