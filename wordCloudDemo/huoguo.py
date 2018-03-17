__author__ = 'mocy'
#coding:UTF-8

import matplotlib.pyplot as plt
import pickle
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
import codecs
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
fin = codecs.open('word1.txt', 'r+', encoding='utf-8')
print(fin.read())
text = ''
with open('word1.txt') as fin:
    for line in fin.readline():
        line = line.strip('\n')
        text += ' '.join(jieba.cut(line))
        text += ' '
fout = open('text.txt','wb')
pickle.dump(text,fout)
fout.close()


fr = open('text.txt','r')
text = pickle.load(fr)
background_Image = plt.imread('girl.jpg')
wc = WordCloud(
    background_color = 'white',
    mask = background_Image,
    max_words = 2000,
    stopwords=STOPWORDS,
    font_path='font.ttf',
    max_font_size=50,
    random_state=30,
)
wc.generate(text)
image_colors = ImageColorGenerator(background_Image)
wc.recolor(color_func=image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()