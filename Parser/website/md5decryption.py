#!/usr/bin/env python2
#!coding:utf-8

import urllib2,urllib
import sys
sys.path.append('..')
import browser_bot

def getResult(cypher, b):
	plantext = ''

	url = 'http://md5decryption.com/'


	data = b.decrypt(url,cypher, {'name':'hash'}, {'name':'submit'})

	if 'Sorry, this MD5 hash wasn\'t found in our database' in data:
		return None
	else:
		plantext = data.split('Decrypted Text:')[1].split('</font>')[1].split('">')[1]
		return plantext


if __name__ == '__main__':
	#p = getResult('b4b147bc522828731f1a016bfa72c073')
	p = getResult('4124bc0a9335c27f086f24ba207a4912')
	print p
