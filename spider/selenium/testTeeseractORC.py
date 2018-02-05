__author__ = 'mocy'
#coding:UTF-8
from PIL import ImageDraw,Image,ImageEnhance,ImageFilter
import pytesseract

#二值判断,如果确认是噪声,用改点的上面一个点的灰度进行替换
#该函数也可以改成RGB判断的,具体看需求如何
def getPixel(image,x,y,G,N):
        L = image.getpixel((x,y))
        if L > G:
            L = True
        else:
            L = False

        nearDots = 0
        if L == (image.getpixel((x - 1,y - 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x - 1,y)) > G):
            nearDots += 1
        if L == (image.getpixel((x - 1,y + 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x,y - 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x,y + 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x + 1,y - 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x + 1,y)) > G):
            nearDots += 1
        if L == (image.getpixel((x + 1,y + 1)) > G):
            nearDots += 1

        if nearDots < N:
            return image.getpixel((x,y-1))
        else:
            return None
def clearNoise(image,G,N,Z):
        draw = ImageDraw.Draw(image)
        for i in range(0,Z):
            for x in range(1,image.size[0] - 1):
                for y in range(1,image.size[1] - 1):
                    color = getPixel(image,x,y,G,N)
                    if color != None:
                        draw.point((x,y),color)

def removeGanrao(im):
        im = im.convert('L')#图像加强，二值化
        sharpness =ImageEnhance.Contrast(im)#对比度增强
        im = sharpness.enhance(2)
        #去除干扰线
        im = im.convert('1')
        data = im.getdata()
        w,h = im.size
        black_point = 0
        for x in range(1,w-1):
            for y in range(1,h-1):
                mid_pixel = data[w*y+x]#中央像素点像素值
                if(mid_pixel==0):
                    top_pixel = data[w*(y-1)+x]
                    left_pixel = data[w*y+(x-1)]
                    down_pixel = data[w*(y+1)+x]
                    right_pixel = data[w*y+(x+1)]
                    if top_pixel==0:
                        black_point+=1
                    if left_pixel==0:
                        black_point+=1
                    if right_pixel==0:
                        black_point+=1
                    if down_pixel==0:
                        black_point+=1
                    if black_point>=3:
                        im.putpixel((x,y),0)
                    black_point = 0
#测试代码
def main():
    #打开图片
    image = Image.open("validate2.jpg")
    #去除干扰线
    removeGanrao(image)
    #将图片转换成灰度图片
    image = image.convert("L")
    sharpness =ImageEnhance.Contrast(image)#对比度增强
    # image = sharpness.enhance(2)
    #去噪,G = 50,N = 4,Z = 4
    clearNoise(image,50,4,4)

    #保存图片
    image.save("code2.jpg")
    image = Image.open("code1.jpg")
    image.load()
    code = pytesseract.image_to_string(image)
    print(code)
if __name__ == '__main__':
    main()