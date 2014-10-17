#!/usr/bin/env python2
#!coding:utf-8

import urllib2,urllib
import sys
sys.path.append('..')
from .. import browser_bot
import time
from selenium import webdriver

def getResult(cypher):
	plantext = ''

	url = 'http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php'

	b = webdriver.Chrome()
	b.get(url)
	b.find_element_by_name('md5').send_keys('\b'*30)
	b.find_element_by_name('md5').send_keys(cypher)
	b.find_element_by_name('md5').submit()
	data = b.page_source
	if 'Hashed string</span>' not in data:
		b.quit()
		return None
	else:
		plantext = data.split('Hashed string</span>: ')[1].split('</')[0]
		b.quit()
		return plantext
	'''
	data = b.decrypt(url,cypher, {'name':'md5'}, {'no':'no'})
	plantext =  data.split('<div id="result"')[1].split('<')[0][1:]
	if 'display: none;' in plantext :
		return None
	else:
		return plantext
	'''
if __name__ == '__main__':
	#p = getResult('b4b147bc522828731f1a016bfa72c073')
	p = getResult('c33367701511b4f6020ec61ded352059')
	print p
