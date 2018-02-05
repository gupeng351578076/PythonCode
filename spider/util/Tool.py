__author__ = 'mocy'
#coding:UTF-8
import re
class Tool:
    #超链接广告剔除
    removeADLink = re.compile('<div class="link_layer.*?</div>')