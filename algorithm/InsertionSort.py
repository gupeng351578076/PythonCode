__author__ = 'mocy'
#coding:UTF-8
source = [92, 77, 67, 8, 6, 84, 55, 85, 43, 67]
for index in range(1,len(source)):
    current_val = source[index]
    position = index

    while position>0 and source[position-1]>current_val:
        source[position] = source[position-1]
        position -= 1
        print(source)

    source[position] = current_val
    # print(source)