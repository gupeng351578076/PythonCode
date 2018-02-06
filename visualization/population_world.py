__author__ = 'mocy'
#coding:UTF-8
import json
import pygal
from pygal.style import LightColorizedStyle,RotateStyle
from pygal_maps_world.maps import World
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2014':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc,pop in cc_populations.items():
    if pop<10000000:
        cc_pops_1[cc] = pop
    elif pop<1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

wm_style = RotateStyle('#336699',base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = '2014年世界人口'
wm.add('1-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)
wm.render_to_file('populationworld.svg')