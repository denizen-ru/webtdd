from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
# browser.get('http://google.com')

assert 'Django' in browser.title
# assert 'Google' in browser.title
