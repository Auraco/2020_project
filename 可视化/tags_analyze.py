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
from wordcloud import WordCloud


tags=[]
words=[]

def get_plt(data, title):
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    fig, ax = plt.subplots()
    ax.barh(range(len(x)), y, color='blue')
    ax.set_yticks(range(len(x)))
    ax.set_yticklabels(x)
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title(title, fontsize=10)
    plt.ylabel("tags")
    plt.xlabel("次数")
    plt.show()

def init_tags():
	with open('bangumi/bgmdb.csv','r',encoding='UTF-8') as csvfile:
		reader = csv.reader(csvfile)
		tags.extend([row[1] for row in reader])
		for i in tags:
			words.extend(re.split(r'\s+',i))
		#print(words)
		counter=Counter()
		for x in words:
			counter[x]+=1
		get_plt(counter.most_common(30),"tags统计top30")

def wordcloud():
	#print(str(words))
	wordscloud=WordCloud(background_color="white",width=1000,height=800,font_path="C:\\Windows\\Fonts\\simsun.ttc",margin=2).generate(str(words))
	plt.imshow(wordscloud)
	plt.axis("off")
	plt.show()


if __name__ == '__main__':
	init_tags()
	wordcloud()
	
