from selenium import webdriver

url = 'https://programwithus.com/learn/python/pip-virtualenv-mac'

browser = webdriver.Chrome()

browser.get(url)

browser.find_element_by_xpath('/html/head/link[9]').click()