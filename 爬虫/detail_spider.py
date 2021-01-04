# -*- coding: utf-8 -*-

import re
import requests
import pandas
import bs4
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import time
import os
import socket
import csv
import json
subjectlist=[]

def init_sub():
	with open('subject_num.csv','r',encoding="utf-8") as csvfile:
		reader = csv.reader(csvfile)
		for one in reader:
			subjectlist.extend(one)

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
    }

bgmdb=[]

def html_save(s):
	with open('bangumi.csv','a') as f:
		f.writer(s+'\n')


def download(bgmsubjects):
	for i in bgmsubjects:
		#print(i)
		url='https://bangumi.tv/subject/'+i
		r = requests.get(url, headers=headers)
		soup = BeautifulSoup(r.content,'lxml', from_encoding='utf-8')
		mainWrapper=soup.find('div',class_='mainWrapper')

		name=soup.find('h1',class_='nameSingle')
		if mainWrapper==None or name==None:
			continue

		infobox=mainWrapper.find('ul',id='infobox')
		if infobox==None:
			continue
		infodict=dict()
		infodict.update({'subject':i,'原名':name.find('a').text if name.find('a')!=None else ''})

		info=infobox.find_all('li')
		for each_info in info:
			kv=each_info.text.split(':',maxsplit=1)
			infodict.update({kv[0].strip():kv[1].strip()})

		tagWrapper=mainWrapper.find('div',class_='inner')
		if tagWrapper==None:
			continue
		tagtext=tagWrapper.select('.l span')
		tags=[]
		for everytag in tagtext:
			tags.append(everytag.text)
		tags=' '.join(tags)
		infodict.update({'tags':tags})
		
		chartWrapper=mainWrapper.find('div',id='ChartWarpper')
		infodict.update({'votes':chartWrapper.find('span',property='v:votes').text})
		rating_list=[]
		for each_rater in chartWrapper.find_all('span',{'class':'count'}):
			rating_list.append(each_rater.text[1:-1])
		infodict.update({'ratings':rating_list})
		overall_score=0
		overall_vote=0
		for score in range(10,0,-1):
			overall_vote+=int(infodict['ratings'][10-score])
			overall_score+=score*int(infodict['ratings'][10-score])
		overall_score=overall_score/overall_vote
		infodict.update({'rating':str('%.3f'%(overall_score))})
		bgmdb.append(infodict)

	path='./bangumi'
	if not os.path.exists(path):
		os.mkdir(path)
	with open(r'bangumi\bgmdb'+'.json','w') as fp:
		json.dump(bgmdb,fp)
	bgmfulldb=pandas.read_json(r'bangumi\bgmdb'+'.json')
	indexs=bgmfulldb[~bgmfulldb.isna()].count().sort_values(ascending=False)[:60].index
	bgmdb2=[]
	for i in bgmdb:
		thisanime=[]
    
		for each_key in indexs:
			if each_key in i.keys():
				thisanime.append(i[each_key])
			else:
				thisanime.append('')
    
		bgmdb2.append(thisanime)
	bgmdb2=pandas.DataFrame(bgmdb2,columns=indexs)
	bgmdb2.to_csv(r'bangumi\bgmdb.csv',index=False)


if __name__ == '__main__':
	init_sub()
	download(subjectlist)