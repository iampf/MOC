#!/usr/bin/env python2

from selenium import webdriver

class BOT:
	def __init__(self):
		self.browser = webdriver.Chrome()

	def decrypt(self, url, cypher, input_text, click_btn):
		self.browser.get(url)
		if input_text.has_key('id'):
			self.browser.find_element_by_id(input_text['id']).send_keys(cypher)
		elif input_text.has_key('name'):
			self.browser.find_element_by_name(input_text['name']).send_keys(cypher)


		if click_btn.has_key('id'):
			self.browser.find_element_by_id(click_btn['id']).click()
		elif click_btn.has_key('name'):
			self.browser.find_element_by_name(click_btn['name']).click()
		data = self.browser.page_source
		self.browser.quit()
		return data

if __name__ == '__main__':
	b = BOT()
	data = b.decrypt('http://md5decryption.com/', '4124bc0a9335c27f086f24ba207a4912', {'name':'hash'}, {'name':'submit'})
	print data
	
