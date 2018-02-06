__author__ = 'mocy'
#coding:UTF-8
from pygal_maps_world.maps import World
worldmap = World()
worldmap.title = 'North,Central,and South America'
worldmap.add('North America',['ca','mx','us'])
worldmap.add('Central America',['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
worldmap.add('South America',['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe', 'py', 'sr', 'uy', 've'])
worldmap.render_to_file('america.svg')
