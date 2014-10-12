#!/usr/bin/env python2
#!coding:utf-8

import urllib2,urllib

def getResult(cypher):
	plantext = ''

	url = 'http://www.md5online.org/'
	req = urllib2.Request(url)
	data = urllib.urlencode({'md5':cypher})
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
	response = opener.open(req,data)
	data = response.read()

	if 'Found : ' in data:
		plantext = data.split('Found : ')[1].split('<b>')[1].split('</b>')[0]
		return plantext
	else:
		return None

	'''

	plantext = data.split('<a')[1].split('">')[1].split('</a>')[0]

	if plantext != '':
		return plantext
	else:
		return None
	'''

if __name__ == '__main__':
	p = getResult('b4b147bc522828731f1a016bfa72c072')
	print p
