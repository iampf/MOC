#!/usr/bin/env python2
#!coding:utf-8

import urllib2,urllib
import sys
sys.path.append('..')
from .. import browser_bot

def getResult(cypher, b):
	plantext = ''

	url = 'http://www.xmd5.org/'

	try:
		data = b.decrypt(url,cypher, {'name':'hash'}, {'name':'xmd5'})
	except:
		return None

	if 'Result:</font>' not in data:
		return None
	else:
		plantext = data.split('Result:</font>')[1].split('Good Luck !')[0].split('\n')[1].split('&gt;')[0].rstrip()
		return plantext

	'''
	plantext = data.split('<span id="ctl00_ContentPlaceHolder1_LabelAnswer">')[1].split('"')[0].split('<')[0]
	if 'Found.But this is a payment record. Hash-type is md5.' in plantext:
		return None
	elif 'Not Found, it had been cracked by our background system' in plantext:
		return None
	else:
		return plantext
	'''
if __name__ == '__main__':
	b = browser_bot.BOT()
	#p = getResult('b4b147bc522828731f1a016bfa72c073')
	p = getResult('b33367701511b4f6020ec61ded352059',b)
	print p
	b.quit()
