__author__ = 'mocy'
#coding:UTF-8
from random import randint
class Die:

    def __init__(self,num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1,self.num_sides)

import pygal
die = Die()
results = []
#随机1000次生成结果
for roll_num  in range(1000):
    result = die.roll()
    results.append(result)
#分析结果
frequencies = []
for value in range(1,die.num_sides):
    frequency = results.count(value)
    frequencies.append(frequency)
#结果可视化
hist = pygal.Bar()
hist.title= "result of rolling  one D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "result"
hist.y_title = "frequency of result"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')