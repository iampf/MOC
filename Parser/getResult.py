#!/usr/bin/env python2
#!coding : utf-8
from browser_bot import BOT
import website.cmd5 as cmd5
import website.haq4u as haq4u
import website.md5_hash as md5_hash
import website.md5decryption as md5decryption
import website.md5online as md5online
import website.myaddr as myaddr
import website.rednoize as rednoize
import website.stringfunction as stringfunction
import website.xmd5 as xmd5

def getResult(cypher):
	print 'Starting Haq4u'
	result = haq4u.getResult(cypher)
	if result != None:
		return result
	print 'Starting md5_hash'
	result = md5_hash.getResult(cypher)
	if result != None:
		return result
	print 'Starting md5online'
	result = md5online.getResult(cypher)
	if result != None:
		return result
	print 'Starting myaddr'
	result = myaddr.getResult(cypher)
	if result != None:
		return result
	b = BOT()
	print 'Starting cmd5'
	result = cmd5.getResult(cypher, b)
	if result != None:
		b.quit()
		return result
	print 'Starting md5decryption'
	result = md5decryption.getResult(cypher, b)
	if result != None:
		b.quit()
		return result

	print 'Starting rednoize'
	result = rednoize.getResult(cypher, b)
	if result != None:
		b.quit()
		return result

	print 'Starting stringfunction'
	result = stringfunction.getResult(cypher, b)
	if result != None:
		b.quit()
		return result
	print 'Starting xmd5'
	result = xmd5.getResult(cypher, b)
	if result != None:
		b.quit()
		return result
