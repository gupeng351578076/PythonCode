__author__ = 'mocy'
#coding:UTF-8
import pygal
from pygal_maps_world.i18n import COUNTRIES
def world_country_map():
    wm_c = pygal.maps.world.World()
    wm_c.force_uri_protocol = 'http'
    wm_c.title = '世界地图'
    for code,name in COUNTRIES.items():
        wm_c.add(name,code)
    wm_c.add('Yemen',{'ye':'Yemen'})
    wm_c.render_to_file('worldmap.svg')
world_country_map()