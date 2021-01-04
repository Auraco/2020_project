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
import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib
from collections import Counter
from pprint import pprint


def ini():
	years=[]
	data=pandas.read_csv('bangumi/bgmdb.csv',encoding='utf-8')
	for year in data['发售日期']:
		temp=str(year)[0:4]
		years.extend([temp])
	count_result = Counter(years)
	count_dict = dict(count_result)
	after=dict(sorted(count_dict.items(), key=lambda x:x[0]))
	#print(after)
	x=list(after.keys())
	y=list(after.values())
	x.pop()
	y.pop()
	plt.figure(figsize = (15, 5))
	matplotlib.rcParams['font.sans-serif'] = ['SimHei']
	plt.title('音乐年制作数量')
	plt.plot(x,y)
	plt.xlabel('年份')
	plt.ylabel('数量')
	plt.show()




if __name__ == '__main__':
	ini()