from selenium import webdriver

browser = webdriver.Chrome()

# url = 'https://programwithus.com/learn/python/pip-virtualenv-mac'
url = 'https://tech-with-tim.teachable.com/p/the-fundamentals-of-programming-with-python'

browser.get(url)

# browser.find_element_by_xpath('/html/head/link[9]').click()
browser.close()
