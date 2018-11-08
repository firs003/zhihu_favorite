#!/usr/bin/python
#coding=utf-8

import os
import requests
import json
from bs4 import BeautifulSoup

def get_json_keys(json):
	keys = []
	for key in json:
		keys.append(key)
	return keys

def get_title_list(json, keys, title):
	names = []
	for key in keys:
		names.append(json[key][title])
	return names

def mkdir_by_title(titles):
	parent = 'zhihu/'
	os.mkdir(parent)
	for title in titles:
		os.mkdir(parent + title)

def get_url_list(json, keys):
	urls = []
	pre = 'https://www.zhihu.com/collection/'
	for key in keys:
		urls.append(pre + key)
	return urls

def get_title_url_list(json):
	pre = 'https://www.zhihu.com/collection/'
	tus = []
	for key in json:
		tus.append({'title':json[key]['title'], 'url':pre + key})
	return tus

print "你好，世界"

headers = {
	# "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"
}

firs003_favourite = requests.get("https://www.zhihu.com/people/firs003/collections/", headers=headers)
# print firs003_favourite.content
soup = BeautifulSoup(firs003_favourite.content, features="html.parser")
# <script id="js-initialData" type="text/json">
json_all_str = soup.find('script', attrs={'id':'js-initialData', 'type':'text/json'}).get_text()
# json_all = soup_init.get_text()
json_all = json.loads(json_all_str)
json_favlists = json_all['initialState']['entities']['favlists']
# print json.JSONEncoder(json_favlists)
# print json_favlists

keys = get_json_keys(json_favlists)
titles = get_title_list(json_favlists, keys, 'title')
urls = get_url_list(json_favlists, keys)
# print urls
# mkdir_by_title(titles)
title_url_list = get_title_url_list(json_favlists)
for tu in title_url_list:
	print tu['title'] + ':' + tu['url']
# for i in range(len(keys)):
# 	# print json_favlists[key]['title']
# 	print str(keys[i]) + json_favlists[keys[i]] + titles[i] + ':' + urls[i]
 	
fav = requests.get("https://www.zhihu.com/collection/102142765", headers=headers)
print fav.content
