__author__ = 'mocy'
import  os
filenames = os.listdir(os.getcwd())
for name in filenames:
    filenames[filenames.index(name)]=name[:-3]
    out = open('names.text','w')
for name in filenames:
    out.write(name+'\n')
out.close()