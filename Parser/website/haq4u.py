#!/usr/bin/env python2
#!coding:utf-8

import urllib2,urllib

def getResult(cypher):
	plantext = ''

	url = 'http://haq4u.com/'
	req = urllib2.Request(url)
	data = urllib.urlencode({'lookup':cypher})
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
	response = opener.open(req,data)
	data = response.read()

	plantext = data.split('<a')[1].split('">')[1].split('</a>')[0]

	if plantext != '':
		return plantext
	else:
		return None


if __name__ == '__main__':
	p = getResult('e10adc3949ba59abbe56e057f20f883a')
