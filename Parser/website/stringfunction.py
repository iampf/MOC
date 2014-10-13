#!/usr/bin/env python2
#!coding:utf-8

import urllib2,urllib
import sys
sys.path.append('..')
import browser_bot

def getResult(cypher, b):
	plantext = ''

	url = 'http://www.stringfunction.com/md5-decrypter.html'


	data = b.decrypt(url,cypher, {'name':'string_md5'}, {'name':'submit'})
	plantext = data.split('<textarea')[1].split('</textarea>')[0].split('">')[1]
	if plantext == '':
		return None
	else:
		return plantext

if __name__ == '__main__':
	p = getResult('b4b147bc522828731f1a016bfa72c073')
	#p = getResult('3f5824a95bd646ead7b5485dabc70583')
	print p
