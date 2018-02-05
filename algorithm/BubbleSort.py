__author__ = 'mocy'
#coding:UTF-8
data_set = [ 9,1,22,31,45,3,6,2,11 ]
loop_count = 0
for j in range(len(data_set)):
    for i in range(len(data_set)-j-1):
        if data_set[i] > data_set[i+1]:
            temp = data_set[i]
            data_set[i]= data_set[i+1]
            data_set[i+1]=temp
        loop_count+=1
print(data_set)
print(loop_count)