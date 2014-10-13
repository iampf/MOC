#!/usr/bin/env python2
#!coding:utf-8

import urllib2,urllib

def getResult(cypher):
	plantext = ''

	url = 'http://www.md5-hash.com/md5-hashing-decrypt/' + cypher
	data = urllib2.urlopen(url).read()

	if 'not found in our database.' in data:
		return None
	else:
		plantext = data.split('title="md5(&#39;')[1].split('&#39;')[0]
		return plantext

	'''
	plantext = data.split('<a')[1].split('">')[1].split('</a>')[0]

	if plantext != '':
		return plantext
	else:
		return None
	'''
if __name__ == '__main__':
	p = getResult('4124bc0a9335c27f086f24ba207a4912')
	print p
