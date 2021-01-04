#encoding=utf8
import requests
from requests.exceptions import RequestException
import re
import os
import pandas
import csv

def get_page(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
url='http://bgm.tv/music/browser?sort=rank'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
    }


def save_data(item):
	with open('subject_num.csv','a',newline='')as f:
		f_csv = csv.writer(f)
		f_csv.writerow(item)

def parse_page(html):
	pattern = re.compile(r'li id="item_(\d+)"')
	items = re.findall(pattern,html)
	save_data(items)

def main(offset):
    url = 'http://bgm.tv/music/browser?sort=rank&page=' + str(offset)
    html = get_page(url)
    parse_page(html)


if __name__ == '__main__':
    	for i in range(5):
    		main(offset=i + 1)
