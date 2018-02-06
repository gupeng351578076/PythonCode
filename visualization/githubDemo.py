__author__ = 'mocy'
#coding:UTF-8
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#获取apijson信息
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dic = r.json()
#分析仓库信息：星统计 描述 链接
repo_dicts = response_dic['items']
names,plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description'])[:200]+'...',
        'xlink':repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

#可视化
my_style = LS('#336699',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45#x轴旋转45度
my_config.show_legend = False#不显示图例
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 24
my_config.truncate_label = 15  # 缩短项目名为15个字符
#my_config.show_minor_y_labels = False  # 隐藏水平线
my_config.width = 1000  # 定义宽度
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
