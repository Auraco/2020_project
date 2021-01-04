# -*- coding: utf-8 -*-

import re
import requests
import pandas
import os
import socket
import csv
import json
from collections import Counter
import matplotlib.pyplot as plt

def get_plt(data, title):
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    plt.figure(figsize = (10, 5))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.bar(x,y)
    plt.title(title, fontsize=10)
    plt.xlabel("作曲")
    plt.ylabel("次数")
    plt.show()

def init_peoples():
	words=[]
	peoples=[]
	with open('bangumi/bgmdb.csv','r',encoding='UTF-8') as csvfile:
		reader = csv.reader(csvfile)
		peoples.extend([row[10] for row in reader])
	for i in peoples:
		words.extend(re.split(r'/|、',i))
	words=list(filter(None, words))
	#print(words)
	
	counter=Counter()
	for x in words:
		counter[x]+=1
	get_plt(counter.most_common(10),"作曲统计top10")


if __name__ == '__main__':
	init_peoples()
	