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

dic={}

def ini():
	data=pandas.read_csv('bangumi/bgmdb.csv',encoding='utf-8')
	years=[]
	for year in data['发售日期']:
		temp=str(year)[0:4]
		years.extend([temp])
	dic['年度']=years
	dic['公司']=data['厂牌']
	

	yr_prod=pandas.crosstab(index=dic['年度'],columns=dic['公司'])
	studios=dic['公司'].dropna().unique()
	studio_dict={}
	for each_studio in studios:
		studio_dict.update({str(each_studio):
			dic['公司'].dropna()[dic['公司'].dropna().str.contains(each_studio)].count()})
	matplotlib.rcParams['font.sans-serif'] = ['SimHei']
	studio_dict=pandas.Series(studio_dict)
	fig = plt.figure(num='company',figsize=(6,6),dpi=200,facecolor='white')
	ax=fig.gca()
	y=studio_dict.sort_values(ascending=False).index.tolist()[:16]
	x=studio_dict.sort_values(ascending=False).values.tolist()[:16]
	ax.pie(x,labels=y,autopct='%.1f%%',pctdistance=0.5,labeldistance=1.1,startangle=120,radius=1.2,counterclock=False,wedgeprops={'linewidth':1.5,'edgecolor':'black'},textprops={'fontsize':10,'color':'black'})
	ax.set_title('音乐制作分布',pad=15)
	plt.show()

if __name__ == '__main__':
	ini()
