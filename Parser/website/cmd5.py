#!/usr/bin/env python2
#!coding:utf-8

import urllib2,urllib
import sys
sys.path.append('..')
from .. import browser_bot

def getResult(cypher, b):
	plantext = ''

	url = 'http://www.cmd5.org/'


	data = b.decrypt(url,cypher, {'id':'ctl00_ContentPlaceHolder1_TextBoxInput'}, {'id':'ctl00_ContentPlaceHolder1_Button1'})
	plantext = data.split('<span id="ctl00_ContentPlaceHolder1_LabelAnswer">')[1].split('"')[0].split('<')[0]
	if 'Found.But this is a payment record. Hash-type is md5.' in plantext:
		return None
	elif 'Not Found, it had been cracked by our background system' in plantext:
		return None
	else:
		return plantext

if __name__ == '__main__':
	#p = getResult('b4b147bc522828731f1a016bfa72c073')
	p = getResult('3f5824a95bd646ead7b5485dabc70583')
	print p
