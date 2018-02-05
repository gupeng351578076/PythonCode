__author__ = 'mocy'
#coding:UTF-8
from lxml import etree
import sys
import io
#改变python3默认输出编码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
text = '''
    <div>
        <ul>
            <li class="item-1"><a href="link1.html">1</a></li>
            <li class="item-2"><a href="link2.html">2</a></li>
            <li class="item-3"><a href="link3.html">3</a></li>
            <li class="item-4"><a href="link4.html">4</a></li>
            <li class="item-5"><a href="link5.html">5</a></li>
            <li class="item-6"><a href="link6.html">6</a></li>
        </ul>
    </div>
'''
html = etree.HTML(text)
print(type(html))
result = etree.tostring(html)
print(result)