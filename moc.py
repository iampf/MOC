#!/usr/bin/env python2
#! coding:utf-8
import sys, optparse
from Parser.getResult import getResult as getResult
def crackMD5(cypher):
	return getResult(cypher)
	

if __name__ == '__main__':
	result = crackMD5(sys.argv[1])
	print result
