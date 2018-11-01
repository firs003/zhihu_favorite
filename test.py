#!/usr/bin/python
#coding=utf-8

import requests

print "你好，世界"

headers = {
	# "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"
}

firs003_favourite = requests.get("https://www.zhihu.com/people/firs003/collections/", headers=headers)
print firs003_favourite.content