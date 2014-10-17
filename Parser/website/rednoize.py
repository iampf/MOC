#!/usr/bin/env python2
#!coding:utf-8

import urllib2,urllib
import sys
sys.path.append('..')
from .. import browser_bot
import time

def getResult(cypher, b):
	plantext = ''

	url = 'http://md5.rednoize.com/'


	data = b.decrypt(url,cypher, {'id':'q'}, {'id':'go'}, timeout=5)
	plantext =  data.split('<div id="result"')[1].split('<')[0][1:]
	if 'display: none;' in plantext :
		return None
	else:
		return plantext
if __name__ == '__main__':
	b = browser_bot.BOT()
	#p = getResult('b4b147bc522828731f1a016bfa72c073')
	p = getResult('e10adc3949ba59abbe56e057f20f883e', b)
	print p
	b.quit()
